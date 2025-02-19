import { useEffect, useState } from "react";
import Header from "../../components/header/Header";
import getLogo from "../../utils/helpers/GetLogo";
import "../prediction/Prediction.css";
import { useParams } from "react-router-dom";
import getTeamAlias from "../../utils/helpers/GetTeamAlias";

export default function Prediction()
{
    const {homeTeam, awayTeam} = useParams();

    const [xGPrediction, setxGPrediction] = useState({});
    const [scorePrediction, setScorePrediction] = useState({});
    const [scoreDistribution, setScoreDistribution] = useState({});
    const [isLoading, setLoading] = useState(true);

    useEffect(() => 
    {
        const fetchData = async () => 
        {
            setLoading(true);

            const xGPredictionResponse = await fetch(`/api/predictions/xG/${homeTeam}/${awayTeam}`);
            const scorePredictionResponse = await fetch(`/api/predictions/score/${homeTeam}/${awayTeam}`);
            const scoreDistributionResponse = await fetch(`/api/predictions/dist/${homeTeam}/${awayTeam}`);

            const xGPredictionData = await xGPredictionResponse.json();
            const scorePredictionData = await scorePredictionResponse.json();
            const scoreDistributionData = await scoreDistributionResponse.json();

            setxGPrediction(xGPredictionData);
            setScorePrediction(scorePredictionData);
            setScoreDistribution(scoreDistributionData);

            setLoading(false);
        };

        fetchData();

    }, [homeTeam, awayTeam]);

    function displayGoalDistribution(distType)
    {
        let selectedDist = {};
        const elements = [];

        switch(distType)
        {
            case 'home': selectedDist = scoreDistribution['home_dist'];
                break;
            case 'away': selectedDist = scoreDistribution['away_dist'];
                break;
        }

        Object.entries(selectedDist).map(([key, value]) => {
            elements.push(
                <li>
                    <p className="goal-amount">{key}</p>
                    <p className="goal-percentage"><b>{(value * 100).toFixed(2)}%</b></p>
                </li>
            )
        })

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
            <section className="prediction-headline">
                <div className="prediction-heading">
                    <h1>Predicted Score</h1>
                </div>
                <div className="fixture-prediction">
                    <div className="fixture-prediction-team">
                        <img src={import.meta.env.BASE_URL + `logos/${getLogo(homeTeam)}`}/>
                        <p>{homeTeam}</p>
                    </div>
                    <div className="fixture-prediction-score">
                        <p><b>{scorePrediction['home_score']} - {scorePrediction['away_score']}</b></p>
                    </div>
                    <div className="fixture-prediction-team">
                        <img src={import.meta.env.BASE_URL + `logos/${getLogo(awayTeam)}`}/>
                        <p>{awayTeam}</p>
                    </div>
                </div>
            </section>
            <section className="prediction-content">
                <div className="xG">
                    <div className="team-xG">
                        <p className="team-xG-label">{getTeamAlias(homeTeam)}'s xG</p>
                        <p className="team-xG-data">{xGPrediction['home_xG']}</p>
                    </div>
                    <div className="team-xG">
                        <p className="team-xG-label">{getTeamAlias(awayTeam)}'s xG</p>
                        <p className="team-xG-data">{xGPrediction['away_xG']}</p>
                    </div>
                </div>
                <div className="distributions">
                    <div className="distributions-container">
                        <h1>
                            {getTeamAlias(homeTeam)}'s
                            <p>Goal Distribution</p>
                        </h1>
                        <ul>
                            {
                                displayGoalDistribution('home')
                            }
                        </ul>
                    </div>
                    <div className="distributions-container">
                        <h1>
                            {getTeamAlias(awayTeam)}'s
                            <p>Goal Distribution</p>
                        </h1>
                        <ul>
                            {
                                displayGoalDistribution('away')
                            }
                        </ul>
                    </div>
                </div>
            </section>
        </>
    )
};