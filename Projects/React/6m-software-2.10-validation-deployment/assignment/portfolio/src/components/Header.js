// React component for header

import photo from '../assets/photo.jpg';

function Header() {
    const imageStyle = {
        width: '300px',
        height: '400px',
        borderRadius: '10px',
        border: '2px solid #333',
        marginTop: '30px',
    };

    return (
        <>
        <img src={photo} alt='photo' style={imageStyle} />
        <h1>Robin Yap</h1>
        <h2>Software Engineer</h2>
        </>
    );
}

export default Header;