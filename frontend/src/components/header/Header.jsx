import React from "react";
import { Link } from "react-router-dom";
import { IconContext } from "react-icons/lib";
import { IoFootballOutline, IoMailOutline, IoMenuOutline } from "react-icons/io5";
import teamMapper from "../../utils/TeamMapper";
import '../header/Header.css';

export default function Header()
{
    function displayLogos()
    {
        const elements = [];

        Object.entries(teamMapper).map(([key, value]) => {
            elements.push(
                <Link key={key} to={`/teams/${key}`}>
                    <img src={import.meta.env.BASE_URL + `logos/${value[1]}`}/>
                </Link>
            )
        });

        return elements;
    };

    function toggleDropdown(e)
    {
        const dropdownMenu = document.querySelector(".dropdown-menu");
        dropdownMenu.classList.toggle("active");
    };

    return (
        <>
            <header>
                <section className="main">
                    <Link to='/'>
                        <IconContext.Provider value={{style: {fontSize: "35px"}, className: "icon"}}>
                            <IoFootballOutline/>
                        </IconContext.Provider>
                    </Link>
                    <div className="nav">
                        <Link to="/" reloadDocument={true}>Home</Link>
                        <Link to="/fixtures" reloadDocument={true}>Fixtures</Link>
                        <Link to="/teams" reloadDocument={true}>Teams</Link>
                    </div>
                    <a href="mailto:harmonyiroha99@gmail.com" className="mail">
                        <IconContext.Provider value={{style: {fontSize: "23px", cursor: "pointer"}, className: "icon"}}>
                            <IoMailOutline/>
                        </IconContext.Provider>
                    </a>
                    <div className="responsive" onClick={toggleDropdown}>
                        <a href="" className="responsive-mail">
                            <IconContext.Provider value={{style: {fontSize: "23px", cursor: "pointer"}, className: "icon"}}>
                                <IoMailOutline/>
                            </IconContext.Provider>
                        </a>
                        <div className="dropdown-btn">
                            <IconContext.Provider value={{style: {fontSize: "30px", cursor: "pointer"}, className: "icon"}}>
                                <IoMenuOutline/>
                            </IconContext.Provider>
                        </div>
                    </div>
                </section>
                <section className="sub" id="sub">
                    <div className="teams-list">
                        {
                            displayLogos()
                        }
                    </div>
                </section>
            </header>
            <section className="dropdown-menu">
                <ul>
                    <Link to="/" reloadDocument={true}><li>Home</li></Link>
                    <Link to="/fixtures" reloadDocument={true}><li>Fixtures</li></Link>
                    <Link to="/teams" reloadDocument={true}><li>Teams</li></Link>
                </ul>
            </section>
        </>
    )
};