import Image from "next/image";
import Link from "next/link";

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

			<div className="bg-[#d4ecff] w-full">
				<div className="flex flex-col items-center justify-center relative space-y-8 py-20">
					<p className="text-[#005eb4] text-5xl tracking-wider">
						What Do we Do?
					</p>
					<p className="text-2xl w-1/2 text-center">
						Our mission at Vitalyte is to harness the power of AI to
						make healthcare more accessible, personalized, and
						efficient for everyone. By combining cutting-edge
						technology with compassionate care, we aim to empower
						individuals to take control of their health journeys,
						leading to better outcomes and healthier lives.
					</p>
				</div>
			</div>

			<div className="w-full mt-12">
				<p className="text-[#005eb4] flex items-center justify-center text-5xl">
					What we have learned
				</p>
				<div className="flex flex-row relative lg:right-32 md:right-24 sm:right-20 right-10 -space-x-40">
					<div className="flex flex-row items-center -space-x-44">
						<div className="relative">
							<img
								src="/imgs/progress_70.png"
								alt=""
								className="h-full w-full z-10"
							/>
							<p className="absolute inset-0 flex items-center justify-center text-4xl font-bold text-black z-40">
								70%
							</p>
						</div>

						<div className="flex flex-col z-40">
							<p className="text-xl font-bold">
								Patients open to using healthcare chatbots
							</p>
							<p className="text-2xl">
								Patients open to using{" "}
								<span className="font-bold text-blue-600">
									healthcare chatbots
								</span>
								for prescription refills, booking appointments,
								and managing their health.
							</p>
						</div>
					</div>

					<div className="flex flex-row items-center -space-x-44">
						<div className="relative">
							<img
								src="/imgs/progress_70.png"
								alt=""
								className="h-full w-full z-10"
							/>
							<p className="absolute inset-0 flex items-center justify-center text-4xl font-bold text-black z-40">
								50%
							</p>
						</div>

						<div className="flex flex-col z-40">
							<p className="text-xl font-bold">
								Healthcare providers invest in digital health
							</p>
							<p className="text-2xl">
								Healthcare providers have increased their
								investment in digital health, including
								<span className="font-bold text-blue-600">
									{" "}
									AI tools
								</span>
								, to support remote patient care and engagement.
							</p>
						</div>
					</div>
				</div>

				<div>
					<div className="flex flex-row items-center justify-center space-x-5">
						<div className="bg-[#d4ecff] h-24 w-48 rounded-full flex items-center justify-center">
							<p className="text-center text-4xl font-extrabold tracking-widest">
								x1.6
							</p>
						</div>
						<p className="text-2xl w-3/4 text-center">
							Children under five in rural areas are 1.6 times
							more likely to die from preventable diseases like
							pneumonia and diarrhea compared to children in urban
							areas.
						</p>
					</div>
				</div>

				<div>
					<div className="flex flex-row items-center justify-center relative right-20">
						<img
							src="/imgs/person_1.png"
							alt=""
							className="h-96 relative"
						/>
						<p className="text-2xl w-1/2">
							The global average physician density in rural areas
							is less than 5 doctors per 10,000 people, compared
							to over 20 in urban areas.
						</p>
					</div>
				</div>

				<div className="bg-[#007698] w-full">
					<div className="flex flex-col items-center justify-center relative space-y-10 py-20">
						<p className="text-5xl text-white">
							Let’s Fight For Accessible Healthcare
						</p>
						<p className="text-2xl text-white">
							Healthcare isn't a need. It's a right.
						</p>

						<Link
							href="/"
							className="bg-[#042839] py-3 px-5 mt-7 hover:text-[#d4ecff] text-white rounded-2xl"
						>
							<p className="text-2xl">Get Vitalyte for Free</p>
						</Link>
					</div>
				</div>

				<div>
					<p className="text-[#005eb4] text-5xl mt-10 flex items-center justify-center">
						Who are We?
					</p>
					<div className="flex-row space-x-20 flex items-center justify-center mt-10 mb-10">
						<Person />
						<Person />
						<Person />
					</div>
				</div>
			</div>
		</div>
	);
}

const Person = () => {
	return (
		<div className="w-[25%] border-4 rounded-3xl relative">
			<div className="">
				<div>
					<img
						src="/imgs/empty_person.png"
						alt=""
						className="object-fill"
					/>
				</div>
				<div className="flex items-center justify-center flex-col">
					<p>Co-Founder</p>
					<p>Anika Samuel</p>
				</div>
			</div>
		</div>
	);
};
