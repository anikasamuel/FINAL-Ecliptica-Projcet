import Image from "next/image";
import Link from "next/link";
import Hover from "@/components/ui/Hover";

export default function About() {
  return (
    <div className="overflow-x-hidden">
      {/* Background section */}
      <div
        className="relative w-full h-screen bg-cover bg-center"
        style={{ backgroundImage: "url(/imgs/background.jpg)" }}
      >
        <div className="absolute inset-0 flex flex-col items-center justify-center z-10">
          <h1 className="text-6xl text-center text-[#005eb4] leading-tight tracking-wider font-bold">
            Our Product <br />
          </h1>
          <p id="what-do-you-want-to-research" className="text-2xl text-black mt-4">
            Accessible expert research. Everywhere.
          </p>
        </div>
      </div>

      {/* Research question section */}
      <div className="w-full bg-[#d4ecff] py-16">
        <p id="possible-data-visualizations" className="text-[#005eb4] text-5xl text-center">
          What Do You Want To Research?
        </p>

        {/* Search bar */}
        <div className="flex justify-center mt-10 mb-16">
          <input
            type="text"
            placeholder="Search research topics..."
            className="px-4 py-2 w-1/2 border border-[#005eb4] rounded-full text-xl focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>
      </div>

      {/* Possible Data Visualizations Section */}
      <Hover />

      {/* Call-to-action section */}
      <div className="bg-[#99ceff] w-full">
        <div className="flex flex-col items-center justify-center relative space-y-10 py-20">
          <p className="text-5xl text-[#005eb4]">
            Let’s Research With the Click of a Button
          </p>
          <p className="text-2xl text-[#005eb4]">
            Compile a list of publications and data visualizations with just one keyword.
          </p>

          <Link
            href="#what-do-you-want-to-research">
            <button className="text-center items-center justify-center center-20 relative bg-[#007698] text-white py-4 px-10 rounded-full text-lg font-medium mt-4 hover:bg-blue-700 transition">
								Explore More About Ecliptica &rarr;
						</button>
          </Link>
        </div>
      </div>
    </div>
  );
}
