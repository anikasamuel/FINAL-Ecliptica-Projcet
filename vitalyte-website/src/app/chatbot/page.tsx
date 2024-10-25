import Link from "next/link";
import { MoveRight } from "lucide-react";
export default function Chatbot() {
	return (
		<div className="mt-20">
			<div className="object-cover w-[115%] relative lg:right-28 md:right-24 sm:right-12 right-10 bottom-10 z-10">
				<img src="/imgs/chatbot_background.png" alt="" className="" />
				<div className="absolute inset-0 flex flex-col items-center justify-center z-40">
					<p className="text-4xl font-bold text-[#005eb4]">
						Explore our Chatbots
					</p>
					{/* <img src="/imgs/doctors_stets.png" alt="" className="h-14 w-32"/> */}
				</div>
			</div>

			<div className="bg-[#007698] w-full">
				<div className="flex flex-col items-center justify-center relative space-y-10 py-20">
					<p className="text-5xl text-white tracking-wider">
						Get Expert Healthcare With Just A Text
					</p>
					<p className="text-white tracking-wider text-xl">
						Use our chatbots to the fullest extent and maximize our
						features.
					</p>

					<Link
						href="/"
						className="bg-[#042839] py-3 px-5 mt-7 hover:text-[#d4ecff] text-white rounded-2xl"
					>
						<p className="text-2xl">Get Vitalyte for Free</p>
					</Link>
				</div>
			</div>
			<div className="mt-10 flex items-center justify-center flex-col lg:-space-y-20 md:-space-x-10 sm:space-x-5 space-x-10">
				<ChatBotComponent />
				<ChatBotComponent />
				<ChatBotComponent />
				<ChatBotComponent />
			</div>
		</div>
	);
}

const ChatBotComponent = () => {
	return (
		<div>
			<div className="flex flex-row space-x-20 items-center justify-center relative right-20">
				<div>
					<img
						src="/imgs/chatbot_empty.png"
						alt=""
						className="object-fill"
					/>
				</div>
				<div className="flex flex-col space-y-10 items-center justify-center right-56 relative w-1/3">
					<p className="text-[#005eb4] text-5xl">Parkinson's</p>
					<p className="text-lg">
						Parkinson's disease is a brain disorder that causes
						shaking, stiffness, and slow movement, making it harder
						to control body movements over time.
					</p>
					<Link
						href="/"
						className="bg-[#d4ecff] py-3 px-5 mt-7 hover:text-[black] text-black rounded-2xl"
					>
						<div className="flex flex-row">
							<p className="text-2xl">Parkinson's Chatbot </p>
							<MoveRight className="w-20 h-10 relative bottom-1" />
						</div>
					</Link>
				</div>
			</div>
		</div>
	);
};
