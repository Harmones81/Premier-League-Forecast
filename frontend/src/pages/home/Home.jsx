import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { IconContext } from "react-icons/lib";
import { IoOpenOutline } from "react-icons/io5";
import getLogo from '../../utils/helpers/GetLogo';
import getTeamAlias from '../../utils/helpers/GetTeamAlias';
import Header from "../../components/header/Header";
import '../home/Home.css';

export default function Home()
{
    const [nextFixture, setNextFixture] = useState({});
    const [nextGameweek, setNextGameweek] = useState([]);
    const [gameweekStatus, setGameweekStatus] = useState({});
    const [isLoading, setLoading] = useState(true);

    useEffect(() => 
    {

        const fetchData = async () => 
        {
            setLoading(true);

            const nextFixtureResponse = await fetch('/api/fixtures/next');
            const nextGameweekResponse = await fetch('/api/fixtures/gameweek/next');
            const gameweekStatusResponse = await fetch('api/status/gameweek');

            const nextFixtureData = await nextFixtureResponse.json();
            const nextGameweekData = await nextGameweekResponse.json();
            const gameweekStatusData = await gameweekStatusResponse.json();

            setNextFixture(nextFixtureData);
            setNextGameweek(nextGameweekData);
            setGameweekStatus(gameweekStatusData);

            setLoading(false);
        }

        fetchData();

    }, []);

    function displayNextGameweek()
    {
        const elements = []

        for(let i = 1; i < 4; i++)
        {
            elements.push(
                <li key={i}>
                    <Link to={`/fixtures/${nextGameweek[i]['Home Team']}/${nextGameweek[i]['Away Team']}`}>
                        <div>
                            <div className="next-gameweek-team">
                                <img src={import.meta.env.BASE_URL + `logos/${getLogo(nextGameweek[i]['Home Team'])}`}/>
                                <div>{nextGameweek[i]['Home Team']}</div>
                            </div>
                            <div className="next-gameweek-team">
                                <img src={import.meta.env.BASE_URL + `logos/${getLogo(nextGameweek[i]['Away Team'])}`}/>
                                <div>{nextGameweek[i]['Away Team']}</div>
                            </div>
                        </div>
                        <div className="next-gameweek-info">
                            <p>{nextGameweek[i]['Date']}</p>
                            <p>{nextGameweek[i]['Time']}</p>
                            <p>Venue: {nextGameweek[i]['Location']}</p>
                        </div>
                    </Link>
                </li>
            )
        }

        return elements;
    };
    
    if(isLoading)
    {
        return (
            <div>Loading...</div>
        )
    }

    return (
        <>
            <Header/>
            <section className="headline">
                <h1><b>Next Fixture</b></h1>
                <div className="next-fixture">
                    <div className="next-fixture-team">
                        <img src={import.meta.env.BASE_URL + `logos/${getLogo(nextFixture['Home Team'])}`}/>
                        <p>{getTeamAlias(nextFixture['Home Team'])}</p>
                    </div>
                    <div className="next-fixture-info">
                        <h1>VS</h1>
                        <p>{nextFixture['Date']} @ {nextFixture['Time']}</p>
                        <p>Venue: {nextFixture['Location']}</p>
                    </div>
                    <div className="next-fixture-team">
                        <img src={import.meta.env.BASE_URL + `logos/${getLogo(nextFixture['Away Team'])}`}/>
                        <p>{getTeamAlias(nextFixture['Away Team'])}</p>
                    </div>
                </div>
                <Link className="next-fixture-link" to={`/fixtures/${nextFixture['Home Team']}/${nextFixture['Away Team']}`}>
                    <button>
                        <IconContext.Provider value={{style: {fontSize: "20px", color: "#38003c"}}}>
                            <IoOpenOutline/>
                        </IconContext.Provider>
                    </button>
                </Link>
            </section>
            <section className="home-content">
                <div className="next-gameweek">
                    <h1>
                        Next Gameweek
                        <p> Gameweek {gameweekStatus['Next']}</p>
                    </h1>
                    <ul>
                        {
                            displayNextGameweek()
                        }
                        <li>
                            <Link className="view-all" to='/fixtures'><button>View All</button></Link>
                        </li>
                    </ul>
                </div>
            </section>
        </>
    )
};