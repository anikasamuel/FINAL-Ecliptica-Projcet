"use client";
import Link from "next/link";
import { useState, useRef, useEffect } from "react";
import { usePathname, useRouter } from "next/navigation";
import { Input } from "@/components/ui/input";
import { Search } from "lucide-react";
import { CircleUserRound } from "lucide-react";

export default function Navbar() {
	const [activeTab, setActiveTab] = useState<string>("home");
	const [isSidebarOpen, setSidebarOpen] = useState(false);
	const [isMediumScreen, setIsMediumScreen] = useState(false);
	const sidebarRef = useRef<HTMLDivElement>(null);
	const pathname = usePathname();
	const router = useRouter();

	const toggleSidebar = () => {
		setSidebarOpen(!isSidebarOpen);
	};

	const handleClickOutside = (event: MouseEvent) => {
		if (
			sidebarRef.current &&
			!sidebarRef.current.contains(event.target as Node)
		) {
			setSidebarOpen(false);
		}
	};

	useEffect(() => {
		if (isSidebarOpen) {
			document.addEventListener("mousedown", handleClickOutside);
		} else {
			document.removeEventListener("mousedown", handleClickOutside);
		}
		return () => {
			document.removeEventListener("mousedown", handleClickOutside);
		};
	}, [isSidebarOpen]);

	useEffect(() => {
		if (pathname) {
			if (pathname === "/") {
				setActiveTab("home");
			} else if (pathname.includes("process")) {
				setActiveTab("process");
			} else if (pathname.includes("mission")) {
				setActiveTab("mission");
			} else if (pathname.includes("about")) {
				setActiveTab("about");
			} else if (pathname.includes("join")) {
				setActiveTab("join");
			} else if (pathname.includes("pricing")) {
				setActiveTab("pricing");
			}
		}
	}, [pathname]);

	useEffect(() => {
		const handleScroll = () => {
			const homeSection = document.getElementById("home");
			const processSection = document.getElementById("process");
			const missionSection = document.getElementById("mission");
			const aboutSection = document.getElementById("about");

			if (aboutSection && window.scrollY >= aboutSection.offsetTop - 50) {
				setActiveTab("about");
			} else if (
				missionSection &&
				window.scrollY >= missionSection.offsetTop - 50
			) {
				setActiveTab("mission");
			} else if (
				processSection &&
				window.scrollY >= processSection.offsetTop - 50
			) {
				setActiveTab("process");
			} else if (
				homeSection &&
				window.scrollY >= homeSection.offsetTop - 50
			) {
				setActiveTab("home");
			}
		};

		window.addEventListener("scroll", handleScroll);

		return () => {
			window.removeEventListener("scroll", handleScroll);
		};
	}, []);

	const handleTabChange = (tab: string) => {
		setActiveTab(tab);
		if (tab != "about" && tab != "join") {
			const section = document.getElementById(tab);
			if (section) {
				section.scrollIntoView({ behavior: "smooth" });
			} else {
				router.push("/");
				setTimeout(() => {
					const section = document.getElementById(tab);
					if (section) section.scrollIntoView({ behavior: "smooth" });
				}, 500);
			}
		}
	};

	return (
		<>
			<header className="fixed inset-0 w-full mx-auto flex z-50 h-10  md:flex items-center">
				<nav className="flex mt-16 h-28 flex-wrap items-center w-full border border-[#3A3A3A] bg-[#d4ecff] p-4 backdrop-blur-xl backdrop-filter">
					<nav
						aria-label="Main"
						data-orientation="horizontal"
						dir="ltr"
						className="relative z-10 flex max-w-max flex-1 items-center justify-between space-x-32"
					>
						<div className="hover:cursor-pointer flex flex-row px-3 space-x-1">
							<div>
								<img
									src="/imgs/logo.png"
									alt=""
									className="h-20 w-20"
								/>
							</div>
							<div className="flex mt-7">
								<p className="text-xl font-bold">Vitalyte</p>
							</div>
						</div>

						<div className="items-center space-x-5 pr-10 hover:cursor-pointer hidden md:flex">
							<a
								href="/"
								className="nav-item hover:text-[#005eb4] hover:rounded-md px-2 mt-1"
							>
								<p className="text-lg">Home</p>
							</a>

							<a
								href="/"
								className="nav-item hover:text-[#005eb4] hover:rounded-md px-2 mt-1 text-lg"
							>
								About
							</a>

							<a
								href="/"
								className="nav-item hover:text-[#005eb4] hover:rounded-md px-2 mt-1 text-lg"
							>
								Chatbots
							</a>

							<a
								href="/"
								className="nav-item hover:text-[#005eb4] hover:rounded-md px-2 mt-1 text-lg"
							>
								Pricing
							</a>

							<a
								href="/"
								className="nav-item hover:text-[#005eb4] px-3 py-0.5 mt-1 bg-[#005eb4] rounded-full text-white tracking-wider text-lg"
							>
								Start for Free
							</a>

							<div className="flex flex-row relative right-4">
								<Search className="h-5 w-5 mt-2 relative left-6" />
								<Input className="border-black rounded-xl w-72" />
							</div>

							<div className="flex flex-row space-x-3 pl-10">
								{/* If user is logged in, display their name */}
								<p className="text-lg">Log In</p>
								<CircleUserRound className="h-7 w-7" />
							</div>
						</div>
					</nav>
				</nav>
			</header>
		</>
	);
}
