import { Link } from  'react-router-dom'

const NavBar = () => {

    return (
    <nav>
        <Link to="/">Home</Link>
        <Link to="/lists/">Lists</Link>
    </nav>
    )
}

export default NavBar;