import React from 'react'
import Navbar from "../components/navbar/navbar_main"
import Participantes from "../components/participantes/participantes_main"
import Footer from "../components/Footer/Footer_main"
import TIntegrantes from "../components/texto_integrantes/tintegrantes_main"



const Integrantes = () => {
    return (
        <div>
            <Navbar />
            <br/>
            <TIntegrantes />
            <Participantes />
            <Footer />
        </div>
    )

};

export default Integrantes;