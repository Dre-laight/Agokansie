import { useContext, useState, useRef, useEffect, } from 'react'
import PageWrapper from '../../../WelcomeScreen/PageWrapper'
import bg from '../../../assets/background-collage.png'
import thinking_image  from '../../../assets/black_man_thinking.webp'
import { ArrowRight, ArrowLeft, CornerDownLeft, CornerDownRight, House} from 'lucide-react'
import { useNavigate } from "react-router-dom";
import woodTapSound from '../../../assets/sound/woodTap.mp3'
import gsap from 'gsap'


function DameLesson4(){

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

    const steps = [{
        step: '1',
        text: "A capture is made by jumping diagonally over an adjacent opponent's piece into the empty square immediately behind it. The jumped piece is then removed from the board.",
        voice: 'Foolish boy Siaw'

    },{
        step: '2',
        text: "Capturing is compulsory in Dame. Whenever a capture is available, you must make it before any other move.",
        voice: 'Foolish boy Siaw'

    },{
        step: '3',
        text: "Regular pieces may move backwards only when performing a legal capture. Backward movement is not allowed during ordinary moves.",
        voice: 'Foolish boy Siaw'

    },{
        step: '4',
        text: "If, after making a capture, another capture is immediately available, you must continue jumping in the same turn until no further captures can be made.",
        voice: 'Foolish boy Siaw'

    } ]

    const [currentStep, setCurrentStep] = useState(0)
    const [nextLesson, setNextLesson] = useState(false)
    const [previousLesson, setPreviousLesson] = useState(false)
    const [previousLessonVariable, setPreviousLessonVariable] = useState(false)

    const previousStep = () => {
        setCurrentStep((previous) => previous === 0 ? previous :  previous - 1)
        console.log(steps[currentStep].step)
        
    }

    const nextStep = () => {
        setCurrentStep((previous) => previous === steps.length - 1 ? previous : previous + 1)
        console.log(steps[currentStep].step)
    }

    const LessonState = () => {
        if(currentStep === steps.length - 1){
            setNextLesson(true)
        } else {
            setNextLesson(false)
        }
    }

    const nextLessonNavigation = () => {
        if (nextLesson){
            navigate('/damelesson5')
        } else {
            nextStep()
        }
    }


    const PreviousLesson = () => {
        if(currentStep === 0){
            setPreviousLessonVariable(true)
        } else {
            setPreviousLessonVariable(false)
        }
    }

    const PreviousLessonNavigation = () => {
        if (previousLessonVariable){
            navigate('/damelesson3')
        } else {
            previousStep()
        }
    }
    

    useEffect(() => {
        LessonState()
        PreviousLesson()
    }, [currentStep])


    const createBoard = () => {
        const board = [];
    
        for (let row = 0; row < 8; row++) {
            const currentRow = [];
    
            for (let col = 0; col < 8; col++) {
                currentRow.push(0);
            }
    
            board.push(currentRow);
        }
    
        return board;
    };
    
    const [board, setBoard] = useState(createBoard);


const pieceRefs = useRef([])
const idx = (row, col) => row * 8 + col
const cellRefs = useRef([])

const step1sequence = [

    // User's piece
    { type: "place", player: 2, row: 5, col: 1 },

    // Opponent's piece to capture
    { type: "place", player: 1, row: 4, col: 2 },

    // Show landing square
    {
        type: "showOptions",
        options: [
            { row: 3, col: 3 }
        ]
    },

    // Perform the capture
    {
        type: "capture",
        player: 2,

        from: { row: 5, col: 1 },

        over: { row: 4, col: 2 },

        to: { row: 3, col: 3 }
    }

];
const step2sequence = [

    // Place player's piece
    {
        type:"place",
        player:2,
        row:5,
        col:1
    },

    // Place opponent piece creating capture
    {
        type:"place",
        player:1,
        row:4,
        col:2
    },


    // Demonstrate available normal move
    {
        type:"showOptions",
        options:[
            {
                row:4,
                col:0
            }
        ]
    },


    // Player attempts normal move
    {
        type:"invalidMove",
        from:{
            row:5,
            col:1
        },
        to:{
            row:4,
            col:0
        }
    },


    // Explain capture is compulsory
    {
        type:"showOptions",
        options:[
            {
                row:3,
                col:3
            }
        ]
    },


    // Perform forced capture
    {
        type:"capture",
        player:2,

        from:{
            row:5,
            col:1
        },

        over:{
            row:4,
            col:2
        },

        to:{
            row:3,
            col:3
        }
    }
];


const step3sequence = [

    // Player 2 piece
    {
        type: "place",
        player: 2,
        row: 5,
        col: 3
    },


    // Player 1 piece behind-right
    {
        type: "place",
        player: 1,
        row: 6,
        col: 4
    },


    // Show illegal backward move
    {
        type: "showOptions",
        options:[
            {
                row:6,
                col:2
            }
        ]
    },


    // Attempt backward movement
    {
        type:"invalidMove",

        from:{
            row:5,
            col:3
        },

        to:{
            row:6,
            col:2
        }
    },


    // Show legal backward capture
    {
        type:"showOptions",
        options:[
            {
                row:7,
                col:5
            }
        ]
    },


    // Perform backward capture
    {
        type:"capture",

        player:2,

        from:{
            row:5,
            col:3
        },

        over:{
            row:6,
            col:4
        },

        to:{
            row:7,
            col:5
        }
    }

];

const step4sequence = [

    {
        type:"place",
        player:2,
        row:6,
        col:2
    },

    {
        type:"place",
        player:1,
        row:5,
        col:3
    },

    {
        type:"place",
        player:1,
        row:3,
        col:5
    },

    {
        type:"showOptions",
        options:[
            {
                row:4,
                col:4
            }
        ]
    },

    {
        type:"capture",
        player:2,

        from:{
            row:6,
            col:2
        },

        over:{
            row:5,
            col:3
        },

        to:{
            row:4,
            col:4
        }
    },


    {
        type:"showOptions",
        options:[
            {
                row:2,
                col:6
            }
        ]
    },


    {
        type:"capture",
        player:2,

        from:{
            row:4,
            col:4
        },

        over:{
            row:3,
            col:5
        },

        to:{
            row:2,
            col:6
        }
    }

];
const stepSequences = {
    '1': step1sequence,
     '2': step2sequence,
     '3': step3sequence,
     '4': step4sequence
}

const runAction = (tl, action, boardState) => {

    switch (action.type) {

        case "place":
            tl.call(() => {
                boardState[action.row][action.col] = action.player;
                setBoard(boardState.map(row => [...row]));
            });

            tl.to({}, { duration: 0.05 });

            tl.call(() => {
                const target = pieceRefs.current[idx(action.row, action.col)];
                if (!target) return;
                gsap.fromTo(target,
                    { scale: 0, y: -30, opacity: 0 },
                    { scale: 1, y: 0, opacity: 1, duration: 0.4, ease: "back.out(2)" }
                );
            });
            break;

        case "move":
            tl.call(() => {
                boardState[action.from.row][action.from.col] = 0;
                boardState[action.to.row][action.to.col] = action.player;
                setBoard(boardState.map(row => [...row]));
            });

            tl.to({}, { duration: 0.05 }); // let React mount the piece at its new cell

            tl.call(() => {
                // the old DOM node is gone — this is a fresh element at the
                // new cell, so it "lands" rather than slides across the board
                const target = pieceRefs.current[idx(action.to.row, action.to.col)];
                if (!target) return;
                gsap.fromTo(target,
                    { scale: 0.6, y: -14, opacity: 0.4 },
                    { scale: 1, y: 0, opacity: 1, duration: 0.3, ease: "back.out(1.7)" }
                );
            });
            break;

        case "invalidMove":
            tl.call(() => {
                const target = pieceRefs.current[idx(action.from.row, action.from.col)];
                if (!target) return;

                const nudgeY = action.to.row < action.from.row ? -8 : 8; // reach toward the attempted direction

                gsap.timeline()
                    .to(target, { y: nudgeY, duration: 0.1 })
                    .to(target, { y: 0, duration: 0.1 })
                    .to(target, {
                        boxShadow: "0 0 15px 4px rgba(255,40,40,0.85)",
                        duration: 0.15
                    }, 0)
                    .to(target, { boxShadow: "none", duration: 0.3 });
            });

            tl.to({}, { duration: 1.2 });
            break;

case "showOptions":
    tl.call(() => {
        (action.options || []).forEach(({ row, col }) => {
            const cell = cellRefs.current[idx(row, col)];
            if (!cell) return; // safety guard

            gsap.to(cell, {
                boxShadow: "inset 0 0 0 4px rgba(124,255,124,0.9)",
                duration: 0.3,
                yoyo: true,
                repeat: 3
            });
        });
    });

    tl.to({}, { duration: 1.6 });
    break;

case "reset":
    tl.call(() => {
        for (let r = 0; r < 8; r++) {
            for (let c = 0; c < 8; c++) {
                if (boardState[r][c] === 0) continue;
                const target = pieceRefs.current[idx(r, c)];
                if (!target) continue;
                gsap.to(target, { scale: 0, opacity: 0, duration: 0.35, ease: "back.in(2)" });
            }
        }
    });

    tl.to({}, { duration: 0.9 });

    tl.call(() => {
        for (let r = 0; r < 8; r++) boardState[r].fill(0);
        setBoard(boardState.map(row => [...row]));
    });

    break;

case "capture":

    // Animate captured piece flying away
    tl.call(()=>{
    const captured = pieceRefs.current[idx(action.over.row, action.over.col)];

    if(captured){
        gsap.to(captured,{
            scale:0,
            opacity:0,
            duration:0.4
        });
    }
});

tl.to({}, {duration:0.45});

tl.call(()=>{
    boardState = boardState.map(row=>[...row]);

    boardState[action.over.row][action.over.col]=0;
    boardState[action.from.row][action.from.col]=0;
    boardState[action.to.row][action.to.col]=action.player;

    setBoard(boardState);
});
    // Wait for React
    tl.to({}, { duration: 0.05 });

    // Animate arriving piece
    tl.call(() => {

        const target =
            pieceRefs.current[idx(action.to.row, action.to.col)];

        if (!target) return;

        gsap.fromTo(
            target,
            {
                scale: 0.6,
                y: -20,
                opacity: 0.5
            },
            {
                scale: 1,
                y: 0,
                opacity: 1,
                duration: 0.35,
                ease: "back.out(1.8)"
            }
        );

    });

    break;

case "compulsoryCapture":

tl.call(()=>{

    const piece =
    pieceRefs.current[idx(action.piece.row, action.piece.col)];

    if(!piece) return;


    gsap.timeline()
    .to(piece,{
        scale:1.15,
        duration:0.2
    })
    .to(piece,{
        scale:1,
        duration:0.2
    });


    action.captureSquares.forEach(({row,col})=>{

        const cell =
        cellRefs.current[idx(row,col)];

        if(!cell) return;


        gsap.to(cell,{
            boxShadow:
            "inset 0 0 0 5px rgba(255,215,0,0.9)",
            duration:0.4,
            repeat:3,
            yoyo:true
        });

    });

});


tl.to({},{
    duration:1.8
});

break;

case "blocked":
    tl.call(() => {

        const piece = pieceRefs.current[idx(action.piece.row, action.piece.col)];

        // Shake the blocked piece
        if (piece) {
            gsap.timeline()
                .to(piece, { x: -8, duration: 0.08 })
                .to(piece, { x: 8, duration: 0.08 })
                .to(piece, { x: -5, duration: 0.08 })
                .to(piece, { x: 5, duration: 0.08 })
                .to(piece, { x: 0, duration: 0.08 });
        }

        // Highlight both blocking pieces
        action.blockers.forEach(({ row, col }) => {
            const blocker = pieceRefs.current[idx(row, col)];
            if (!blocker) return;

            gsap.fromTo(
                blocker,
                {
                    boxShadow: "0 0 0 rgba(255,120,0,0)"
                },
                {
                    boxShadow: "0 0 18px rgba(255,120,0,0.9)",
                    duration: 0.3,
                    repeat: 3,
                    yoyo: true
                }
            );
        });

    });

    tl.to({}, { duration: 1.8 });
    break;

    case "backwardCaptureNotice":

tl.call(()=>{

    const piece =
    pieceRefs.current[idx(action.piece.row, action.piece.col)];


    if(piece){

        gsap.timeline()
        .to(piece,{
            scale:1.15,
            duration:0.2,
            ease:"power2.out"
        })
        .to(piece,{
            scale:1,
            duration:0.2
        });

    }


    action.captureSquares.forEach(({row,col})=>{

        const cell =
        cellRefs.current[idx(row,col)];


        if(!cell) return;


        gsap.to(cell,{
            boxShadow:
            "inset 0 0 0 5px rgba(0,255,100,0.9)",
            duration:0.4,
            repeat:3,
            yoyo:true
        });

    });

});


tl.to({},{
    duration:1.5
});

break;

}

};

useEffect(() => {
    const currentSequence = stepSequences[steps[currentStep].step]
    if (!currentSequence) return;

    let boardState = createBoard();

    const tl = gsap.timeline({
        repeat: -1,
        repeatDelay: 2,
        onRepeat: () => {
            boardState = createBoard();
            setBoard(boardState);
        }
    });

    currentSequence.forEach(action => {
        runAction(tl, action, boardState);
        tl.to({}, { duration: 1 });
    });

    return () => {
        tl.kill();
        resetOptions()
        setBoard(createBoard());
    };

}, [currentStep]);

const resetOptions = () => {
    cellRefs.current.forEach(cell => {
        if (!cell) return;
        gsap.killTweensOf(cell);
        gsap.set(cell, { boxShadow: "none" });
    });
};




return(
<PageWrapper>
    <div className='absolute inset-0 bg-linear-to-r from-[#d4a017]/80 via-[#8b5a2b]/70 to-[#3b1f0f]/80 -z-1 min-h-screen flex flex-col items-center justify-center'>
        <img src={bg} alt="background image" className="absolute object-cover w-full h-full -z-1 opacity-[0.3]"/>   
    </div> 

    <div className='flex flex-col h-screen w-full'>

    <div className="absolute top-0 right-0 flex items-center gap-4 z-50 bg-dark/50 p-3 rounded-bl-lg">
        <ArrowLeft className=' left-3 size-8 cursor-pointer text-midGold' onClick={goBack} />
        <ArrowRight className=' size-8 text-gold-300 cursor-pointer text-midGold' onClick={goForward} />
        <House className=' size-7 text-gold-300 cursor-pointer text-midGold' onClick={() => {navigate('/selectionScreen')}}/>

    </div>


    <div className='flex flex-row items-start gap-4 p-6 shrink-0 ' >
        
            <img src={thinking_image} className='h-40 mt-15'/>

            <div>
                {/* <div>
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
                </div> */}
                        
                <div className='relative w-[50%] shadow-lg rounded-lg p-3 text-[17px] backdrop-blur-md text-white bg-dark/30 mt-20 -ml-10'>
                    <p>{steps[currentStep].text}</p>
                </div>
                
            </div>          
        </div>

        <button onClick={nextLessonNavigation} className='absolute bottom-5 right-5 border-none p-3 text-xl rounded-lg cursor-pointer bg-gradient-to-br from-[#A47551] to-[#6B4226] text-[#F7E7CE] uppercase font-bold hover:scale-95 transition-smooth duration-300 flex items-center justify-center gap-3 bg-dark/30'> 
            <p>{nextLesson ? 'Next Lesson' : 'Next'}</p>
            <CornerDownRight /> 
        </button>

        <button onClick={PreviousLessonNavigation} className='absolute bottom-5 left-5 border-none p-3 text-xl rounded-lg cursor-pointer bg-gradient-to-br from-[#A47551] to-[#6B4226] text-[#F7E7CE] uppercase font-bold hover:scale-95 transition-smooth duration-300 flex items-center justify-center gap-3'> 
            <CornerDownLeft /> 
            <p>{previousLessonVariable ? 'Previous Lesson' : 'Previous'}</p>
        </button>

    
       <div className='absolute left-1/2 -translate-x-1/2 border-2 border-t-0 border-midGold rounded-br-lg rounded-bl-lg px-6 py-2 text-center bg-dark/90 text-darkgold shadow-midGold shadow-sm '>

            <div>
                <p className='uppercase text-3xl font-bold font-fingerpaint'>Capturing pieces</p>
            </div>

            <div className='flex items-center justify-between'>
                <p className=' text-midGold'>Lesson 4</p>
                <p className='text-midGold'>{`Step ${steps[currentStep].step}`}</p>
            </div>
            
        </div>

         <div className="absolute inset-0 flex items-center justify-center mt-35 -z-1 scale-90">
                     <div className="grid grid-cols-8 border-4 border-gray-900 ">
                    {board.map((row, rowIndex) =>
                        row.map((square, colIndex) => (
                    <div
                        ref={(el) => (cellRefs.current[idx(rowIndex, colIndex)] = el)}
                        key={`${rowIndex}-${colIndex}`}
                        className={`${
                        (rowIndex + colIndex) % 2 === 0
                    ? "bg-gold"
                    : "bg-dark"
                    } h-16 w-16 border flex items-center justify-center`}
        >
            {square !== 0 && (
                <div
                    ref={(el) => (pieceRefs.current[idx(rowIndex, colIndex)] = el)}
                    className={`size-9 rounded-full ${
                        square === 1
                            ? "bg-black"
                            : "bg-red-600"
                    }`}
                />
            )}
        </div>
    ))
)}
                </div>            
            </div>
        
        

        
    
    </div>
</PageWrapper>


)
}

export default DameLesson4