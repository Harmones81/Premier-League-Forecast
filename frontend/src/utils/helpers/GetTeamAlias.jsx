import teamMapper from "../TeamMapper";

/**
 * @param {string} team 
 */
export default function getTeamAlias(team)
{
    return teamMapper[team][0];
};