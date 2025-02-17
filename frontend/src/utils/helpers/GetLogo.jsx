import teamMapper from "../TeamMapper";

/**
 * @param {string} team 
 */
export default function getLogo(team)
{
    return teamMapper[team][1];
};