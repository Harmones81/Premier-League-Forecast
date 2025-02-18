import { useEffect, useState } from "react";
import Header from "../../components/header/Header";
import Banner from "../../components/banner/Banner";
import getLogo from "../../utils/helpers/GetLogo";
import getTeamAlias from "../../utils/helpers/GetTeamAlias";
import teamMapper from "../../utils/TeamMapper";
import "../teams/Teams.css";
import { Link } from "react-router-dom";
import { IconContext } from "react-icons/lib";
import { IoArrowForwardOutline } from "react-icons/io5";

export default function Teams()
{
    const [teams, setTeams] = useState([]);
    const [isLoading, setLoading] = useState(true);

    useEffect(() => 
    {
        const fetchData = async () => 
        {
            setLoading(true);

            const teamsResponse = await fetch('/api/teams');
            const teamsData = await teamsResponse.json();
            setTeams(teamsData);

            setLoading(false);
        };

        fetchData();

    }, []);

    function displayTeams()
    {
        const elements = [];

        for(let i = 0; i < teams.length; i++)
        {
            elements.push(
                <TeamContainer 
                    name={getTeamAlias(teams[i]['Team'])} 
                    img={import.meta.env.BASE_URL + `logos/${getLogo(teams[i]['Team'])}`}
                    primaryColor={teamMapper[teams[i]['Team']][2]}
                    secondaryColor={teamMapper[teams[i]['Team']][3]}
                />
            )
        }

        return elements;
    }

    if(isLoading)
    {
        return (
            <div>Loading...</div>
        )
    }

    return (
        <>
            <Header/>
            <Banner primaryColor={"#3cacfc"} secondaryColor={"#5c84fc"}>
                <h1>Teams</h1>
            </Banner>
            <section className="teams-content">
                <div className="teams-container">
                    <ul className="teams">
                        {
                            displayTeams()
                        }
                    </ul>
                </div>
            </section>
        </>
    )
};

function TeamContainer({name, img, primaryColor, secondaryColor})
{
    const [hover, setHover] = useState(false);

    const normalStyles = 
    {
        borderRadius: `5px`,
        background: `repeating-linear-gradient(
                        45deg, 
                        #f2f2f2, 
                        #f2f2f2 80px, 
                        #cecdcd 80px, 
                        #cecdcd 160px)`,
        border: `3px solid rgb(205, 205, 205)`,
        flex: `1 1 300px`,
        transition: `ease, 0.35s all`
    };

    const hoverStyles =
    {
        background: `repeating-linear-gradient(
                        45deg, 
                        ${primaryColor}, 
                        ${primaryColor} 80px, 
                        ${secondaryColor} 80px, 
                        ${secondaryColor} 160px)`,
    }

    return (
        <li
            onMouseEnter={() => setHover(true)}
            onMouseLeave={() => setHover(false)}
            style={{...normalStyles, ...(hover ? hoverStyles : null)}}
        >
            <Link to={`/teams/${name}`}>
                <div className="team-logo">
                    <img src={img}/>
                </div>
                <div className="team-name">
                    <h1>{name}</h1>
                    <span>
                        <IconContext.Provider value={{style: {fontSize: "18px"}}}>
                            <IoArrowForwardOutline/>
                        </IconContext.Provider>
                    </span>
                </div>
            </Link>
        </li>
    )
};