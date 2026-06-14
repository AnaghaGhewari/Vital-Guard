import { NavLink, Outlet, useNavigate } from 'react-router-dom'
import { useAuth } from '../context/AuthContext.jsx'

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
        <p>VitalGuard</p>
        <nav aria-label="Protected pages">
          <NavLink to="/dashboard">Dashboard</NavLink>{' '}
          <NavLink to="/add-vitals">Add Vitals</NavLink>{' '}
          <NavLink to="/risk-history">Risk History</NavLink>
        </nav>
        <p>{userId ? `Signed in as user #${userId}` : 'Signed in'}</p>
        <button type="button" onClick={handleLogout}>
          Logout
        </button>
      </header>

      <Outlet />
    </div>
  )
}

export default ProtectedLayout
