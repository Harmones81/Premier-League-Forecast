/**
 * @param {Array} arr (Array of dictionaries)
 * @param {string} key
 */

export default function groupByKey(arr, key)
{
    const grouped = {}

    // Grouping objects by the given key
    arr.forEach(obj => 
    {
        const keyValue = obj[key];

        if (!grouped[keyValue]) 
        {
            grouped[keyValue] = [];
        }

        grouped[keyValue].push(obj);
    });

    // Convert the object values into a 2D array
    return Object.values(grouped);
};