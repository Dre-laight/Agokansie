    import React from "react";
    import PageWrapper from "./PageWrapper";

    import dameBg from '../assets/checkersBg.png'
    import owareBg from '../assets/owareBg.png'
    import achiBg from '../assets/achiBg.png'
    import bg2 from '../assets/bg_selection.png'

    import { useState, useRef} from 'react'
    import { getAnimatableNone } from "framer-motion";
    import { ChevronRight, ChevronLeft } from 'lucide-react'

    import swipeSound from '../assets/sound/uiSwipeSound.mp3'



    function SelectionScreen() {
        const games = [
            {key: 0, name: 'Oware',  backgroundImage: owareBg,},
            {key: 1, name: 'Dame', backgroundImage: dameBg,  },
            {key: 2, name: 'Achi',   backgroundImage: achiBg,  }
        ]

        const [current, setCurrent] = useState(0)
        const audio = new Audio(swipeSound)

    
        const nextGame = () => {
            setCurrent((previous) => (previous + 1) % games.length)
            audio.play()
    
        }

        const previousGame = () => {
            setCurrent( (previous) => 
                previous === 0 ? games.length - 1 : previous - 1)
                audio.play()
        }


        return (
            <PageWrapper>
                <div className="relative flex h-screen w-full items-center justify-center overflow-x-hidden">

                    {/* background image */}
                         <img src={games[current].backgroundImage} alt="background image" className="absolute object-cover w-full h-full blur-[3px]"/>   
                   

                    <div className="flex flex-col gap-15 justify-center items-center z-10 h-screen">
                        {/* <div className="mb-20">
                            <p className="uppercase font-elite font-bold text-white text-7xl select-none">what do you want to play?</p>

                        </div> */}

                        <div className="w-screen flex justify-between items-center z-10 ">
                                


                            {/* previous toggle */}
                            <ChevronLeft className='size-30 text-gold cursor-pointer ml-3 animate-previous' onClick={previousGame} strokeWidth={1}/>


                            {/* Game text*/}
                                <p className="uppercase font-kablammo font-bold text-darkgold text-9xl select-none">
                                {
                                    games[current].name.split("").map((letter, index) => (
                                        <span
                                            key={index}
                                            className="animate-float inline-block"
                                            style={{animationDelay: `${index * 0.1}s`}}
                                        >
                                            {letter}
                                        </span>
                                    ))
                                
                                }</p>

                            {/* next toggle */}
                            <ChevronRight className="size-30 text-gold cursor-pointer mr-3 animate-next" onClick={nextGame} strokeWidth={1}/>    

                        </div>


                        {/* selection buttons */}
                        <div className="flex items-center justify-center gap-8 ">
                            <button className="border-none p-3 w-40 text-xl text-d rounded-lg cursor-pointer bg-gradient-to-br from-[#A47551] to-[#6B4226] text-[#F7E7CE] uppercase font-bold hover:text-2xl transition-smooth duration-300" >Play</button>

                            <button className="border-none p-3 w-40 text-xl text-d rounded-lg cursor-pointer bg-gradient-to-br from-[#A47551] to-[#6B4226] text-[#F7E7CE] uppercase font-bold hover:text-2xl transition-smooth duration-300">Tutorial</button>
                        </div>
                        
                    </div>


                    
                </div>

            </PageWrapper>
        
        )   
    }

    export default SelectionScreen