import { useEffect, useState } from "react";
import Header from "../../components/header/Header";
import Banner from "../../components/banner/Banner";
import getLogo from "../../utils/helpers/GetLogo";
import groupByKey from "../../utils/helpers/GroupByKey";
import getTeamAlias from "../../utils/helpers/GetTeamAlias";
import "../fixtures/Fixtures.css";
import { Link } from "react-router-dom";
import { IconContext } from "react-icons/lib";
import { IoLocationOutline } from "react-icons/io5";

export default function Fixtures()
{
    const [fixtures, setFixtures] = useState([]);
    const [isLoading, setLoading] = useState(true);

    useEffect(() => 
    {
        const fetchData = async () =>
        {
            setLoading(true);

            const fixturesResponse = await fetch('/api/fixtures');
            const fixturesData = await fixturesResponse.json();
            const sortedFixtures = groupByKey(fixturesData, 'Gameweek');

            setFixtures(sortedFixtures);

            setLoading(false);
        };

        fetchData();

    }, []);

    function displayFixtures()
    {
        const elements = [];

        elements.push(
            fixtures.map((group, index) => (
                <div key={index} className="gameweek-fixtures">
                    <h1>Gameweek {fixtures[index][0]["Gameweek"]}</h1>
                    <ul>
                        {
                            group.map((item, idx) => (
                                <li key={idx}>
                                    <Link>
                                        <div className="fixture-teams">
                                            <div className="fixture-team">
                                                <p><b>{getTeamAlias(item["Home Team"])}</b></p>
                                                <img src={import.meta.env.BASE_URL + `logos/${getLogo(item['Home Team'])}`}/>
                                            </div>
                                            <div className="fixture-time">
                                                <p>{item["Time"]}</p>
                                            </div>
                                            <div className="fixture-team">
                                                <img src={import.meta.env.BASE_URL + `logos/${getLogo(item['Away Team'])}`}/>
                                                <p><b>{getTeamAlias(item["Away Team"])}</b></p>
                                            </div>
                                        </div>
                                        <div className="fixture-date">
                                            <p>{item['Date']}</p>
                                        </div>
                                        <div className="fixture-location">
                                            <p>
                                                <IconContext.Provider value={{style: {fontSize: ""}}}>
                                                    <IoLocationOutline/>
                                                </IconContext.Provider>
                                                {item['Location']}
                                            </p>
                                        </div>
                                    </Link>
                                </li>
                            ))
                        }
                    </ul>
                </div>
            ))
        )

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
                <h1>Fixtures</h1>
            </Banner>
            <section className="fixtures-content">
                <div className="fixtures">
                    {
                        displayFixtures()
                    }
                </div>
            </section>
        </>
    )
};