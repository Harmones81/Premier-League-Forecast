import React from "react";
import { Link } from "react-router-dom";
import logoMapper from '../../utils/LogoMapper';
import '../header/Header.css';
import { IconContext } from "react-icons/lib";
import { IoFootballOutline, IoLogoGithub, IoLogoLinkedin, IoMailOutline, IoMenuOutline } from "react-icons/io5";

export default function Header()
{
    function displayLogos() 
    {
        const elements = [];
        
        Object.entries(logoMapper).map(([key, value]) => {
            elements.push(
                <Link key={key} to={`/teams/${key}`}>
                    <img src={import.meta.env.BASE_URL + `images/logos/${value}`}/>
                </Link>
            )
        });

        return elements;
    };

    return (
        <header>
            <section className="main-header">
                <Link to="/">
                    <IconContext.Provider value={{style: {fontSize: "35px"}, className: "header-icon"}}>
                        <IoFootballOutline/>
                    </IconContext.Provider>
                </Link>
                <div className="nav">
                    <Link to="/" reloadDocument={true}>Home</Link>
                    <Link to="/fixtures" reloadDocument={true}>Fixtures</Link>
                    <Link to="/results" reloadDocument={true}>Results</Link>
                    <Link to="/table" reloadDocument={true}>Table</Link>
                </div>
                <div className="socials">
                    <a href="mailto:harmonyiroha99@gmail.com">
                        <IconContext.Provider value={{style: {fontSize: "23px"}, className: "header-icon"}}>
                            <IoMailOutline/>
                        </IconContext.Provider>
                    </a>
                </div>
            </section>

            <section className="sub-header" id="sub-header">
                {
                    displayLogos()
                }
            </section>
        </header>
    )
};