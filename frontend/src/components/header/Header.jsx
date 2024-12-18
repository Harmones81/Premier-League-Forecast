import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import "../header/Header.css";
import { IconContext } from "react-icons/lib";
import { IoFootballOutline, IoLogoGithub, IoLogoLinkedin, IoMailOutline } from "react-icons/io5";

const Header = () => {
    const [images, setImages] = useState([]);

    useEffect(() => {
        fetch('http://127.0.0.1:5000/teams')
            .then(response => response.json())
            .then(data => setImages(data));
    }, []);

    const displayTeamLogos = () => {
        const elements = [];

        for(let i = 0; i < images.length; i++)
        {
            let src = images[i].Logo;
            let splitSrc = src.split("\\");
            let finalSrc = splitSrc[1];
            console.log(finalSrc);

            elements.push(
                <Link to="" key={i}>
                    <img src={`http://localhost:5000/serve/images/${finalSrc}`}/>
                </Link>
            );
        }

        return elements;
    }

    return (
        <header>
            <section className="main-header">
                <Link to="/">
                    <IconContext.Provider value={{style: {fontSize: "35px"}, className: "header-icon"}}>
                        <IoFootballOutline/>
                    </IconContext.Provider>
                </Link>
                <div className="page-nav">
                    <Link>Home</Link>
                    <Link>Fixtures</Link>
                    <Link>Results</Link>
                    <Link>Table</Link>
                </div>
                <div className="socials-nav">
                    <a href="mailto:harmonyiroha99@gmail.com">
                        <IconContext.Provider value={{style: {fontSize: "25px"}, className: "header-icon"}}>
                            <IoMailOutline/>
                        </IconContext.Provider>
                    </a>
                    <a href="https://github.com/Harmones81" target="_blank">
                        <IconContext.Provider value={{style: {fontSize: "25px"}, className: "header-icon"}}>
                            <IoLogoLinkedin/>
                        </IconContext.Provider>
                    </a>
                    <a href="https://www.linkedin.com/in/harmony-iroha/" target="_blank">
                        <IconContext.Provider value={{style: {fontSize: "25px"}, className: "header-icon"}}>
                            <IoLogoGithub/>
                        </IconContext.Provider>
                    </a>
                </div>
            </section>
            <section className="sub-header" id="sub-header">
                {
                    displayTeamLogos()
                }
            </section>
        </header>
    )
};

export default Header;