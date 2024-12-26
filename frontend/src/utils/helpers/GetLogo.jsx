import logoMapper from "../LogoMapper";

/**
 * @param {string} team 
 */
export default function getLogo(team)
{
    return logoMapper[team];
};