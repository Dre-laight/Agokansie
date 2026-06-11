import { createContext, useState } from "react";
import dameBg from '../assets/checkersBg.png'
import owareBg from '../assets/owareBg.png'
import achiBg from '../assets/achiBg.png'

export const GameContext = createContext()

export const GameProvider = ({children}) => {

    const [currentGame, setCurrentGame] = useState(0)

     const games = [
                {key: 0, name: 'Oware',  backgroundImage: owareBg,},
                {key: 1, name: 'Dame', backgroundImage: dameBg,  },
                {key: 2, name: 'Achi',   backgroundImage: achiBg,  }
            ]

    return(
        <GameContext.Provider
            value={{
                games,
                currentGame,
                setCurrentGame  
            }}
            >
            {children}
        </GameContext.Provider>
    )
}