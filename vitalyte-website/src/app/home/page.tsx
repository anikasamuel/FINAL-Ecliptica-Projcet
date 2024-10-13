import Image from "next/image";
import Head from "next/head";
import Link from "next/link";

export default function Home() {
	return (
		<>
			<Head>
				<title>Innovative Technology. Empowering Healthcare.</title>
				<meta
					name="description"
					content="Vitalyte: Built for your healthcare experience, simplified by AI."
				/>
			</Head>
			<div className="min-h-screen flex items-center justify-center bg-white">
				<div className="flex lg:flex-row lg:items-start w-full">
					<div className="lg:w-1/2 space-y-6 m-auto px-20">
						<h1 className="text-6xl text-center text-[#005eb4] leading-tight tracking-wider font-bold">
							Innovative Technology. <br />
							Empowering Healthcare.
						</h1>
						<p className="text-center text-2xl text-gray-800 tracking-wider w-3/4 left-10 relative">
							Meet{" "}
							<span className="font-bold text-[#007698]">
								Vitalyte
							</span>
							. Built for your healthcare experience, simplified
							by{" "}
							<span className="font-bold text-[#007698]">AI</span>
							.
						</p>
						<button className="text-center items-center justify-center left-20 relative bg-[#007698] text-white py-4 px-10 rounded-full text-lg font-medium mt-4 hover:bg-blue-700 transition">
							Learn about us &rarr;
						</button>
					</div>

					{/* Change this later so that on smaller screens the img becomes the background */}
					<div
						className="mt-12 top-1 left-16 relative w-[100vw] h-[100vh] bg-cover bg-center"
						style={{ backgroundImage: "url(/imgs/home_logo.svg)" }}
					/>
				</div>
			</div>

			<div className="bg-[#d4ecff] h-[100vh] w-full relative bottom-12">
				<div className="flex justify-center items-center top-12 relative flex-col">
					<h1 className="text-center text-5xl tracking-wider text-[#005eb4] leading-relaxed">
						Ready to manage your health <br />
						<span className="">with just a conversation?</span>
					</h1>

					<p className="mt-5 text-2xl tracking-wide w-1/2 text-center">
						Use our health chatbots and{" "}
						<span className="font-black text-[#007698]">
							revitalize yourself
						</span>{" "}
						with expert recommendations and patient help.{" "}
					</p>

					<Link
						href="/"
						className="bg-[#007698] py-2 px-5 mt-7 hover:text-[#d4ecff] text-white rounded-full"
					>
						<p className="text-2xl">Get Vitalyte for Free</p>
					</Link>

					<div className="flex flex-row space-x-2 mt-7">
						<p className="text-2xl">Already have an account?</p>
						<p className="text-2xl underline">
							<Link href="/">Log in</Link>
						</p>
					</div>
				</div>
			</div>

			<div className="flex justify-start w-full">
				<img
					src="/imgs/chatbot.svg"
					className=""
					alt="Chatbot illustration"
				/>
			</div>
		</>
	);
}
