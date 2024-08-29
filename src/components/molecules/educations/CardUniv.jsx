import { useEffect, useRef } from "react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { IoIosArrowRoundForward } from "react-icons/io";

gsap.registerPlugin(ScrollTrigger);

const CardUniv = () => {
  const cardRef = useRef(null);

  useEffect(() => {
    gsap.fromTo(
      cardRef.current,
      { opacity: 0, y: 50 },
      {
        opacity: 1,
        y: 0,
        duration: 1,
        ease: "power3.out",
        scrollTrigger: {
          trigger: cardRef.current,
          start: "top 80%", // When the top of the card is 80% from the top of the viewport
          end: "bottom 20%", // When the bottom of the card is 20% from the top of the viewport
          toggleActions: "play none none none",
        },
      }
    );
  }, []);

  return (
    <>
      <div ref={cardRef} className="flex items-center gap-2 w-full max-w-5xl border-black border-2 rounded-md p-2 mb-4 shadow-[4.0px_8.0px_8.0px_rgba(0,0,0,0.38)]">
        <img src="/images/ubhara.png" alt="Education" className="w-14 h-14" />
        <div className="w-full max-w-2xl">
          <p className="font-montserrat text-3 font-semibold smm:hidden">
            Full Stack Developer
          </p>
          <p className="font-montserrat text-3 font-semibold hidden smm:block">
            Full Stack Developer
          </p>
          <p className="font-montserrat text-2">Bachelor of Computer Science</p>
        </div>
        <div
          className="w-10"
          onClick={() => document.getElementById("modalName").showModal()}
        >
          <IoIosArrowRoundForward className="w-10 h-10 cursor-pointer border-y border-x border-black rounded-full animate-pulse hover:scale-125 transition duration-300 ease-in-out" />
        </div>
      </div>

      {/* Modal Content */}
      <dialog
        id="modalName"
        className="modal"
        onClick={(e) => e.target.close()}
      >
        <div
          className="modal-box bg-primary rounded"
          onClick={(e) => e.stopPropagation()}
        >
          <form method="dialog">
            <button className="btn btn-sm btn-circle btn-ghost absolute right-2 top-2">
              ✕
            </button>
          </form>
          <h3 className="font-montserrat font-bold text-lg mb-6">
            Hello there!
          </h3>
          <img
            src="/images/ubhara.png"
            alt="Tech Stack"
            className="w-24 mb-2"
          />
          <p className="font-montserrat">
            A full-stack web developer is a person who can develop both client and server software. In addition to mastering HTML and CSS, he/she also knows how to: Program a browser Program a server
          </p>
        </div>
      </dialog>
    </>
  );
};

export default CardUniv;
