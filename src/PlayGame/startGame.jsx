import { useContext, useState, useRef, useEffect } from 'react'
import PageWrapper from '../WelcomeScreen/PageWrapper'
import { GameContext } from '../context/GameContext'
import thinking_image  from '../assets/black_man_thinking.webp'
import bg from '../assets/background-collage.png'
import woodTapSound from '../assets/sound/woodTap.mp3'


function GameScreen(){
    const {games, currentGame} = useContext(GameContext)

    const thinking = "..."

    const [beadCount, setBeadCount] = useState(4)

    const [leftOverBeads, setLeftOverBeads] = useState(0)

    const [boardValueList, setBoardValueList] = useState([])


    const woodTap = useRef(new Audio(woodTapSound))

    const OutOfPlay = ({leftOverBeads}) => {
        return(
            <>

                <div className='flex flex-wrap items-center justify-center gap-1 p-4'>
                    {Array.from({length: leftOverBeads}).map((_, index) => (
                                        <div key={index}
                                            className='rounded-full bg-gradient-to-br from-grey-500 to-green-200 size-4'></div>
                                    ))}
                </div>
               
            </>
    
        )
    }

    const Pit = ({beadCount}) => {
        return(
            <>
                 <div className="w-27 h-27 rounded-full bg-[#5c3317] shadow-inner flex flex-wrap items-center justify-center gap-1 p-4">
                    <div className='grid grid-cols gap-1 justify-items-center items-center'></div>                        
                    {Array.from( {length: beadCount }).map((_, index) =>(
                        <div key={index}
                        className='rounded-full bg-gradient-to-br from-grey-600 to-green-300 size-4'></div>

                    ))}
                </div>
            </>

        )
    }

    const getRequest = async () => {
            try {
                const response = await fetch('http://192.168.88.40:5000/api/game/state')

                if(!response.ok){
                    throw new Error('Request failed')
                }

                const BoardData = await response.json()
                setBoardValueList(BoardData.board)
                console.log(BoardData.board)
            }

            catch (error) {
                console.log(error.message)
            }

               
        }

    useEffect(() => {
        getRequest()
    }, [])

    const getBoardState = () => {
        getRequest()

        woodTap.current.currentTime = 0
        woodTap.current.play()
    }   

    return(
        <PageWrapper >
            
            <div className='absolute inset-0 bg-gradient-to-r from-[#3b1f0f]/80 via-[#8b5a2b]/70 to-[#d4a017]/80 -z-1 min-h-screen flex flex-col items-center justify-center'>
                <img src={bg} alt="background image" className="absolute object-cover w-full h-full -z-1 opacity-[0.3]"/>   
        </div>

        <div className='flex flex-col h-screen w-full'>

       
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

            <div className="flex-1 flex items-center justify-center">

                <div className="flex flex-col items-center">

                    <div className="w-67 h-22 bg-[#6b3f1d] border-4 border-b-0 border-[#4a2a12] rounded-t-[3rem] shadow-2xl flex items-center justify-center gap-3 p-4">
                        <div className="w-65 h-17 bg-[#5c3317] rounded-t-[3rem] shadow-2xl flex items-center justify-center gap-3 p-4">
                            <OutOfPlay leftOverBeads={boardValueList[12]}/>
                        </div>
                    </div>

                    <div className="bg-[#8b5a2b] p-6 border-x-4 border-[#5a3418] shadow-2xl rounded-4xl">

                    <div className="flex gap-4 mb-5">

                        <Pit beadCount={boardValueList[0]}/>
                        <Pit beadCount={boardValueList[1]}/>
                        <Pit beadCount={boardValueList[2]}/>
                        <Pit beadCount={boardValueList[3]}/>
                        <Pit beadCount={boardValueList[4]}/>
                        <Pit beadCount={boardValueList[5]}/>


                    </div>

                    <div className="flex gap-4">

                        <Pit beadCount={boardValueList[6]}/>
                        <Pit beadCount={boardValueList[7]}/>
                        <Pit beadCount={boardValueList[8]}/>
                        <Pit beadCount={boardValueList[9]}/>
                        <Pit beadCount={boardValueList[10]}/>
                        <Pit beadCount={boardValueList[11]}/>

                    </div>

                    </div>

                    <div className="w-67 h-22 bg-[#6b3f1d] border-4 border-t-0 border-[#4a2a12] rounded-b-[3rem] shadow-2xl flex items-center justify-center gap-3 p-4">
                        <div className="w-65 h-17 bg-[#5c3317] rounded-b-[3rem] flex items-center justify-center gap-3 p-4">
                            <OutOfPlay leftOverBeads={boardValueList[13]}/>

                    </div>
                    </div>

                    <button onClick={getBoardState} className='absolute bottom-5 right-5 border-none p-3 w-40 text-xl rounded-lg cursor-pointer bg-gradient-to-br from-[#A47551] to-[#6B4226] text-[#F7E7CE] uppercase font-bold hover:text-[19px] transition-smooth duration-300'>I've played</button>

            </div>

            </div>
            </div>
            
        </PageWrapper>
        
    )   
}

export default GameScreen