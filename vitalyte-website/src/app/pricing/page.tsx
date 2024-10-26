export default function Pricing() {
	return (
		<div className="mt-20 overflow-x-hidden">
			<div className="object-cover w-[115%] relative lg:right-28 md:right-24 sm:right-12 right-10 bottom-10 z-10">
				<img src="/imgs/background_bckg.png" alt="" className="" />
				<div className="absolute inset-0 flex flex-col items-center justify-center z-40 space-y-5">
					<p className="text-6xl font-bold text-[#005eb4]">
						Make Vitalyte Right For You
					</p>
					<p className="text-xl tracking-wider text-center w-1/3 relative">
						Explore our pricing plans to elevate your personalized
						experience.
					</p>
				</div>
			</div>

			<div className="flex items-center justify-center px-20 flex-row space-x-20">
				<PricingComponent />
				<PricingComponent />
			</div>
		</div>
	);
}

const PricingComponent = () => {
	return (
		<div className="border-2 border-[#d1e4f7] rounded-xl w-3/4 p-6 mb-20">
			<div className="flex flex-col space-y-4">
				<p className="text-blue-600 text-xl font-semibold">Free</p>
				<p className="text-4xl font-bold">$0/month</p>
				<p className="text-gray-600 text-sm">Summary of plan.</p>

				<button className="bg-[#e0f0ff] text-blue-600 py-2 px-4 rounded-lg font-semibold hover:bg-[#cfe4ff] transition">
					Get Started for Free
				</button>

				<div className="space-y-2 mt-4">
					{Array.from({ length: 5 }).map((_, index) => (
						<div
							key={index}
							className="flex items-center space-x-2"
						>
							<span className="text-blue-600 text-lg">✔️</span>
							<p className="text-gray-700">Feature</p>
						</div>
					))}
				</div>
			</div>
		</div>
	);
};
