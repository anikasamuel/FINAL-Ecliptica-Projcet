library(dplyr)
library(readr)
library(tm)
library(topicmodels)
library(SnowballC)

# Capture the command line arguments
args <- commandArgs(trailingOnly = TRUE)
if (length(args) < 2) {
  stop("Two arguments must be provided: input CSV and output Rdata prefix")
}

input_file <- args[1]
output_rdata_prefix <- args[2]

# Print args for debug
cat("Arguments provided:\n")
print(args)

# Set working directory to script location (safe default)
setwd(dirname(normalizePath(input_file)))
cat("Working directory set to:\n")
print(getwd())

# Load and filter data
data <- read_csv(input_file, show_col_types = FALSE)

if (!"Abstract" %in% colnames(data)) {
  stop("Input file must have an 'Abstract' column.")
}

data <- data %>% filter(!is.na(Abstract) & nchar(Abstract) > 0)
cat("✅ Loaded and filtered data, remaining rows:", nrow(data), "\n")

# Create corpus
corp <- VCorpus(VectorSource(data$Abstract)) %>%
  tm_map(content_transformer(tolower)) %>%
  tm_map(removePunctuation, ucp = TRUE) %>%
  tm_map(removeNumbers) %>%
  tm_map(removeWords, c(stopwords("english"), "food", "security", "insecurity")) %>%
  tm_map(stemDocument) %>%
  tm_map(stripWhitespace)

# Tokenizer
BigramTokenizer <- function(x) {
  words_list <- words(x)
  bigrams <- unlist(lapply(ngrams(words_list, 2), paste, collapse = "_"), use.names = FALSE)
  c(words_list, bigrams)
}

# Create DTM
dtm <- DocumentTermMatrix(corp, control = list(tokenize = BigramTokenizer))
sparse_val <- max(0.1, 1 - 10/nrow(dtm))
dtm <- removeSparseTerms(dtm, sparse = sparse_val)
cat("✅ Document-term matrix created, terms:", ncol(dtm), "docs:", nrow(dtm), "\n")

if (ncol(dtm) == 0 || nrow(dtm) == 0) {
  stop("DTM is empty after sparsity filtering. Try adjusting the sparsity threshold or check your data.")
}

# Output directory
output_dir <- file.path(getwd(), "CTMmods")
if (!dir.exists(output_dir)) dir.create(output_dir)

# Run CTM (non-parallel)
ks <- 5
for (k in ks) {
  cat("📌 Running CTM with", k, "topics...\n")
  ctm <- CTM(dtm, k = k, method = 'VEM')
  output_path <- file.path(output_dir, paste0("ctm", k, ".Rdata"))
  save(ctm, file = output_path)
  cat("✅ Saved model to", output_path, "\n")
}
