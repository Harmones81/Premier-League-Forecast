import { useEffect, useState } from "react";
import Header from "../../components/header/Header";
import Banner from "../../components/banner/Banner";
import getLogo from "../../utils/helpers/GetLogo";
import "../team/Team.css";
import { useParams } from "react-router-dom";
import teamMapper from "../../utils/TeamMapper";

export default function Team()
{
    const {team} = useParams();

    const [data, setData] = useState({});
    const [statistics, setStatistics] = useState({});
    const [isLoading, setLoading] = useState(true);

    useEffect(() => 
    {
        const fetchData = async () => 
        {
            setLoading(true);

            const dataResponse = await fetch(`/api/teams/${team}`);
            const statisticsResponse = await fetch(`/api/statistics/${team}`);

            const dataJson = await dataResponse.json();
            const statisticsJson = await statisticsResponse.json();

            setData(dataJson);
            setStatistics(statisticsJson);

            setLoading(false);
        };

        fetchData();

    }, [team]);

    if(isLoading)
    {
        return (
            <div>Loading...</div>
        )
    }

    return (
        <>
            <Header/>
            <Banner primaryColor={teamMapper[team][2]} secondaryColor={teamMapper[team][3]}>
                <div className="team-banner">
                    <img src={import.meta.env.BASE_URL + `logos/${getLogo(team)}`}/>
                    <h1>{team}</h1>
                </div>
            </Banner>
            <section className="team-content">
                <div className="basic-stats">
                    <div className="stat">
                        <p className="stat-label">Matches Played</p>
                        <p className="stat-data">{data['MP']}</p>
                    </div>
                    <div className="stat">
                        <p className="stat-label">Wins</p>
                        <p className="stat-data">{data['W']}</p>
                    </div>
                    <div className="stat">
                        <p className="stat-label">Draws</p>
                        <p className="stat-data">{data['D']}</p>
                    </div>
                    <div className="stat">
                        <p className="stat-label">Losses</p>
                        <p className="stat-data">{data['L']}</p>
                    </div>
                    <div className="stat">
                        <p className="stat-label">Goals</p>
                        <p className="stat-data">{data['GF']}</p>
                    </div>
                    <div className="stat">
                        <p className="stat-label">Goals Conceded</p>
                        <p className="stat-data">{data['GA']}</p>
                    </div>
                </div>
                <div className="detailed-stats">
                    <div className="detailed-stats-container">
                        <h1>Offensive Stats</h1>
                        <ul>
                            <li>
                                <p>Goals</p>
                                <p><b>{data['GF']}</b></p>
                            </li>
                            <li>
                                <p>Goals per match</p>
                                <p><b>{data['GF'] / data['MP']}</b></p>
                            </li>
                            <li>
                                <p>Attack rating</p>
                                <p><b>{statistics['att_rating']}</b></p>
                            </li>
                        </ul>
                    </div>
                    <div className="detailed-stats-container">
                        <h1>Defensive Stats</h1>
                        <ul>
                            <li>
                                <p>Goals conceded</p>
                                <p><b>{data['GA']}</b></p>
                            </li>
                            <li>
                                <p>Goals conceded per match</p>
                                <p><b>{data['GA'] / data['MP']}</b></p>
                            </li>
                            <li>
                                <p>Defense rating</p>
                                <p><b>{statistics['def_rating']}</b></p>
                            </li>
                        </ul>
                    </div>
                </div>
            </section>
        </>
    )
};