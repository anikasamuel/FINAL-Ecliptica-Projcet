import Image from "next/image";
import Head from "next/head";

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
		</>
	);
}
