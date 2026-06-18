import { NavLink, Outlet, useNavigate } from 'react-router-dom'
import { useAuth } from '../context/AuthContext.jsx'
import logo from '../assets/vitalguard-shield.png'

function ProtectedLayout() {
  const navigate = useNavigate()
  const { logout, userId } = useAuth()

  const handleLogout = () => {
    logout()
    navigate('/login', { replace: true })
  }

  return (
    <div>
      <header>
        <div className="navbar-brand">
         <img
          src={logo}
          alt="VitalGuard"
          className="navbar-brand__logo"
        />
         <span>VitalGuard</span>
       </div>
        
        <nav aria-label="Protected pages">
          <NavLink to="/dashboard">Dashboard</NavLink>{' '}
          <NavLink to="/add-vitals">Add Vitals</NavLink>{' '}
          <NavLink to="/risk-history">Risk History</NavLink>
        </nav>
        <div className="navbar-user">
          <div className="navbar-user__avatar">VG</div>

           <div className="navbar-user__info">
             <span>Welcome Back</span>
           </div>
          </div>
        <button type="button" onClick={handleLogout}>
          Logout
        </button>
      </header>

      <Outlet />
    </div>
  )
}

export default ProtectedLayout
