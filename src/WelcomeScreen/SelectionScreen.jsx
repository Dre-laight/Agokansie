    import PageWrapper from "./PageWrapper";
    import GameScreen from "../PlayGame/startGame";
    

    import { useState, useRef, useContext} from 'react'
    import { ChevronRight, ChevronLeft } from 'lucide-react'
    import { GameContext } from "../context/GameContext";

    import swipeSound from '../assets/sound/uiSwipeSound.mp3'
    import woodTapSound from '../assets/sound/woodTap.mp3'
    import { useNavigate } from "react-router-dom";



    function SelectionScreen() {
       
        const {games, currentGame, setCurrentGame} = useContext(GameContext)
        const swipeAudio = useRef(new Audio(swipeSound))

    
        const nextGame = () => {
            setCurrentGame((previous) => (previous + 1) % games.length)
            swipeAudio.current.currentTime = 0
            swipeAudio.current.play()
    
        }

        const previousGame = () => {
            setCurrentGame( (previous) => 
                previous === 0 ? games.length - 1 : previous - 1)
                swipeAudio.current.currentTime = 0  
                swipeAudio.current.play()
        }

        const navigate = useNavigate()
        const woodTap = useRef(new Audio(woodTapSound))


        const startGame = () => {

            async function sendPostRequest(){
                try {
                    const response = await fetch('http://192.168.88.29:5000/game-type', {
                    method: 'POST',
                    headers: {
                        'Content-Type': "application/json",
                    },
                    body: JSON.stringify(
                            { game_choice: games[currentGame].name}
                        )

                })

                } catch (error) {
                    console.log(error)
                }
            }
                sendPostRequest()

                navigate('/gameScreen')

                woodTap.current.currentTime = 0
                woodTap.current.play()  
                
        }



        return (
            <PageWrapper>
                <div className="relative flex h-screen w-full items-center justify-center overflow-x-hidden">

                    {/* background image */}
                         <img src={games[currentGame].backgroundImage} alt="background image" className="absolute object-cover w-full h-full"/>   
                   

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
                                    games[currentGame].name.split("").map((letter, index) => (
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
                            <button className="border-none p-3 w-40 text-xl text-d rounded-lg cursor-pointer bg-gradient-to-br from-[#A47551] to-[#6B4226] text-[#F7E7CE] uppercase font-bold hover:text-2xl transition-smooth duration-300" onClick={startGame} >Play</button>

                            <button className="border-none p-3 w-40 text-xl text-d rounded-lg cursor-pointer bg-gradient-to-br from-[#A47551] to-[#6B4226] text-[#F7E7CE] uppercase font-bold hover:text-2xl transition-smooth duration-300">Tutorial</button>
                        </div>
                        
                    </div>   
                </div>

            </PageWrapper>
        
        )   
    }

    export default SelectionScreen