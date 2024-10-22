import Image from "next/image";
export default function About() {
	return (
		// Fix up background bug
		<div className="overflow-x-hidden">
			<div className="object-cover w-[115%] relative lg:right-28 md:right-24 sm:right-12 right-10 bottom-10 z-10">
				<img src="/imgs/about_background.svg" alt="" className="" />
				<div className="absolute inset-0 flex flex-col items-center justify-center z-40">
					<p className="text-4xl font-bold text-[#005eb4]">
						About Us
					</p>
					<p className="text-2xl text-black mt-4">
						Accessible healthcare. Everywhere.
					</p>
				</div>
			</div>

			<div className="bg-[#d4ecff] w-full h-80">
				<div className="flex flex-col items-center justify-center top-20 relative space-y-8">
					<p className="text-[#005eb4] text-4xl">What Do we Do?</p>
					<p className="text-xl w-1/2 text-center">
						Our mission at Vitalyte is to harness the power of AI to
						make healthcare more accessible, personalized, and
						efficient for everyone. By combining cutting-edge
						technology with compassionate care, we aim to empower
						individuals to take control of their health journeys,
						leading to better outcomes and healthier lives.
					</p>
				</div>
			</div>
		</div>
	);
}
