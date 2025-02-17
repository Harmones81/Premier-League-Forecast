import "../banner/Banner.css";

export default function Banner({children, primaryColor, secondaryColor})
{
    const gradientStyle = 
    {
        background: `repeating-linear-gradient(
                        45deg, 
                        ${primaryColor}, 
                        ${primaryColor} 80px, 
                        ${secondaryColor} 80px, 
                        ${secondaryColor} 160px)`
    };

    return (

        <section className="banner" style={gradientStyle}>
            {children}
        </section>

    )
};