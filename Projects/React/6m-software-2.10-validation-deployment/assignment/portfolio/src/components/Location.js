// React component for location

import flag from '../assets/flag.jpg';

function Location() {
    const imageStyle = {
        width: '300px',
        height: '200px',
        borderRadius: '10px',
        border: '2px solid #333',
        marginTop: '10px',
        marginBottom: '30px',
    };

    return (
        <>
            <h3>Location</h3>
            <hr />
            <p>Singapore</p>
            <img src={flag} alt='flag' style={imageStyle} />
        </>
    );
}

export default Location;