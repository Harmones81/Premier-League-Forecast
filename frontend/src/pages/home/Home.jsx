import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import getLogo from '../../utils/helpers/GetLogo';
import Header from "../../components/header/Header";
import Footer from "../../components/footer/Footer";
import '../home/Home.css';

export default function Home()
{
    const [teams, setTeams] = useState([]);
    const [nextFixture, setNextFixture] = useState({});
    const [nextGameweek, setNextGameweek] = useState([]);
    const [fixtureResults, setFixtureResults] = useState([]);
    const [isLoading, setLoading] = useState(true);

    useEffect(() => 
    {

        const fetchData = async () => 
        {
            setLoading(true);

            const teamsResponse = await fetch('/api/teams');
            const nextFixtureResponse = await fetch('/api/fixtures/next');
            const nextGameweekResponse = await fetch('/api/fixtures/gameweek/18');
            const fixtureResultsResponse = await fetch('/api/fixtures/played');

            const teamData = await teamsResponse.json();
            const nextFixtureData = await nextFixtureResponse.json();
            const nextGameweekData = await nextGameweekResponse.json();
            const fixtureResultsData = await fixtureResultsResponse.json();

            setTeams(teamData);
            setNextFixture(nextFixtureData);
            setNextGameweek(nextGameweekData);
            setFixtureResults(fixtureResultsData);

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
                <li>
                    <Link to={`/fixtures/${nextGameweek[i]['Home Team']}/${nextGameweek[i]['Away Team']}`}>
                        <div>
                            <div className="next-gameweek-team">
                                <img src={import.meta.env.BASE_URL + `images/logos/${getLogo(nextGameweek[i]['Home Team'])}`}/>
                                <div>{nextGameweek[i]['Home Team']}</div>
                            </div>
                            <div className="next-gameweek-team">
                                <img src={import.meta.env.BASE_URL + `images/logos/${getLogo(nextGameweek[i]['Away Team'])}`}/>
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

    function displayRecentResults()
    {
        const elements = []
        const start = fixtureResults.length - 3;

        for(let i = start; i < fixtureResults.length; i++)
        {
            elements.push(
                <li>
                    <div className="fixture-result">
                        <div className="fixture-result-team">
                            <img src={import.meta.env.BASE_URL + `images/logos/${getLogo(fixtureResults[i]['Home Team'])}`}/>
                            <p>{fixtureResults[i]['Home Team']}</p>
                        </div>
                        <div className="scoreline">
                            <p>{fixtureResults[i]['Result']}</p>
                        </div>
                        <div className="fixture-result-team">
                            <img src={import.meta.env.BASE_URL + `images/logos/${getLogo(fixtureResults[i]['Away Team'])}`}/>
                            <p>{fixtureResults[i]['Away Team']}</p>
                        </div>
                    </div>
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
                <h1>Next Fixture</h1>
                <div className="next-fixture">
                    <div className="next-fixture-team">
                        <img src={import.meta.env.BASE_URL + `images/logos/${getLogo(nextFixture['Home Team'])}`}/>
                        <p>{nextFixture['Home Team']}</p>
                    </div>
                    <div className="next-fixture-info">
                        <h1>VS</h1>
                        <p>{nextFixture['Date']} @ {nextFixture['Time']}</p>
                        <p>Venue: {nextFixture['Location']}</p>
                    </div>
                    <div className="next-fixture-team">
                        <img src={import.meta.env.BASE_URL + `images/logos/${getLogo(nextFixture['Away Team'])}`}/>
                        <p>{nextFixture['Away Team']}</p>
                    </div>
                </div>
            </section>

            <section className="content">
                <div className="next-gameweek">
                    <h1>
                        Next Gameweek
                        <p>Gameweek 18</p> {/* Replace Gameweek # with an actual value*/}
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

                <div className="recent-results">
                    <h1>
                        Recent Results
                        <p>Last 3 Fixtures</p>
                    </h1>
                    <ul>
                        {
                            displayRecentResults()
                        }

                        <li>
                            <Link className="view-all" to='/results'><button>View All</button></Link>
                        </li>
                    </ul>
                </div>
            </section>

            <Footer/>
        </>
    )
};