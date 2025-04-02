"use client";
import Link from "next/link";
import { useState, useEffect } from "react";
import { usePathname } from "next/navigation";

export default function Navbar() {
	const [activeTab, setActiveTab] = useState<string>("home");
	const pathname = usePathname();

	useEffect(() => {
		if (pathname === "/") {
			setActiveTab("home");
		} else if (pathname.includes("about")) {
			setActiveTab("about");
		}
	}, [pathname]);

	return (
		<header className="fixed inset-0 w-full mx-auto flex z-50 h-10 md:flex items-center">
			<nav className="flex mt-16 h-28 flex-wrap items-center w-full border border-[#3A3A3A] bg-[#007698] p-4 backdrop-blur-xl backdrop-filter justify-between">
				<Link href="/" className="hover:cursor-pointer flex flex-row px-3 space-x-1">
					<img src="/imgs/logo.jpg" alt="Ecliptica Logo" className="h-20 w-20" />
					<div className="flex mt-7">
						<p className="text-xl font-bold text-white">Ecliptica</p>
					</div>
				</Link>

				<div className="items-center space-x-16 pr-20 hover:cursor-pointer hidden md:flex">
					<a href="/" className="nav-item hover:text-[#d4effc] hover:rounded-md px-2 mt-1 text-lg text-white">
						Home
					</a>
					<a href="/about" className="nav-item hover:text-[#d4effc] hover:rounded-md px-2 mt-1 text-lg text-white">
						Our Product
					</a>
				</div>
			</nav>
		</header>
	);
}
