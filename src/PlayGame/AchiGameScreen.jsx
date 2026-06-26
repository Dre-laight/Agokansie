import { useContext, useState, useRef, useEffect, } from 'react'
import PageWrapper from '../WelcomeScreen/PageWrapper'
import bg from '../assets/background-collage.png'
import thinking_image  from '../assets/black_man_thinking.webp'
import { ArrowRight, ArrowLeft } from 'lucide-react'
import { useNavigate } from "react-router-dom";
import woodTapSound from '../assets/sound/woodTap.mp3'



function AchiGame(){

const woodTap = useRef(new Audio(woodTapSound))
const thinking = "..."

const navigate = useNavigate()



const goBack = () => {
        navigate(-1)
        woodTap.current.currentTime = 0
        woodTap.current.play()
    }

const goForward = () => {
    navigate(1)
    woodTap.current.currentTime = 0
    woodTap.current.play()
}

const getBoardState = () => {
    console.log('i have played')
}




return(
<PageWrapper>
    <div className='absolute inset-0 bg-linear-to-r from-[#3b1f0f]/80 via-[#8b5a2b]/70 to-[#d4a017]/80 -z-1 min-h-screen flex flex-col items-center justify-center'>
        <img src={bg} alt="background image" className="absolute object-cover w-full h-full -z-1 opacity-[0.3]"/>   
    </div> 

    <div className='flex flex-col h-screen w-full'>

    <div className="absolute top-0 right-0 flex items-center gap-4 z-50 backdrop-blur p-3 rounded-lg">
        <ArrowLeft className=' left-3 size-8 cursor-pointer text-wood ' onClick={goBack} />
        <ArrowRight className=' size-8 text-gold-300 cursor-pointer text-wood' onClick={goForward} />
    </div>


    <div className='flex flex-row items-start gap-4 p-6 shrink-0' >
        
        <img src={thinking_image} className='h-40'/>

        <div>
            <div>
                <p className='text-4xl text-white'>
                    {
                        thinking.split("").map((dot, index) => (
                            <span
                                key={index}
                                style={{animationDelay: `${index * 0.2}s`}}
                                className='inline-block animate-float'
                            >{dot}
                            </span>
                        ))
                    }
                </p>
            </div>
                    
            <div className='relative w-[50%] shadow-lg rounded-lg p-3 text-[17px] backdrop-blur-md text-white'>
                <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Itaque, quae sit sint culpa rerum possimus magni? Dolorum vero dolores, facere qui porro facilis?</p>
            </div>
            
        </div>
        </div>

            <div class="flex flex-col items-center justify-center mt-20">
            <div class="relative h-96 w-96 border-2 bg-radial from-gold to-wood">

                <div class="absolute left-1/3 top-0 h-full w-[2px] -translate-x-1/2 bg-black"></div>
                <div class="absolute left-2/3 top-0 h-full w-[2px] -translate-x-1/2 bg-black"></div>


                <div class="absolute top-1/3 left-0 h-[2px] w-full -translate-y-1/2 bg-black"></div>
                <div class="absolute top-2/3 left-0 h-[2px] w-full -translate-y-1/2 bg-black"></div>


                <div class="absolute left-0 top-0 h-[2px] w-[136%] origin-top-left rotate-45 bg-black"></div>
                <div class="absolute right-0 top-0 h-[2px] w-[136%] origin-top-right -rotate-45 bg-black"></div>


                <div class="grid h-full w-full grid-cols-3 grid-rows-3">
                <div class="flex items-center justify-center">
                    <div class="h-6 w-6 rounded-full bg-black"></div>
                </div>

                <div class="flex items-center justify-center">
                    <div class="h-6 w-6 rounded-full bg-black"></div>
                </div>

                <div class="flex items-center justify-center">
                    <div class="h-6 w-6 rounded-full bg-black"></div>
                </div>

                <div class="flex items-center justify-center">
                    <div class="h-6 w-6 rounded-full bg-black"></div>
                </div>

                <div class="flex items-center justify-center">
                    <div class="h-6 w-6 rounded-full bg-black"></div>
                </div>

                <div class="flex items-center justify-center">
                    <div class="h-6 w-6 rounded-full bg-black"></div>
                </div>

                <div class="flex items-center justify-center">
                    <div class="h-6 w-6 rounded-full bg-black"></div>
                </div>

                <div class="flex items-center justify-center">
                    <div class="h-6 w-6 rounded-full bg-black"></div>
                </div>

                <div class="flex items-center justify-center">
                    <div class="h-6 w-6 rounded-full bg-black"></div>
                </div>
                </div>
            </div>
            </div>

        <button onClick={getBoardState} className='absolute bottom-5 right-5 border-none p-3 w-40 text-xl rounded-lg cursor-pointer bg-gradient-to-br from-[#A47551] to-[#6B4226] text-[#F7E7CE] uppercase font-bold hover:scale-95 transition-smooth duration-300'>I've played</button>

        
    
    </div>
</PageWrapper>


)
}

export default AchiGame