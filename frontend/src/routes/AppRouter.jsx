import {
  createBrowserRouter,
  createRoutesFromElements,
  Navigate,
  Outlet,
  Route,
  RouterProvider,
} from 'react-router-dom'
import ProtectedRoute from '../components/ProtectedRoute.jsx'
import ProtectedLayout from '../components/ProtectedLayout.jsx'
import { useAuth } from '../context/AuthContext.jsx'
import AddVitalsPage from '../pages/AddVitalsPage.jsx'
import DashboardPage from '../pages/DashboardPage.jsx'
import LoginPage from '../pages/LoginPage.jsx'
import RegisterPage from '../pages/RegisterPage.jsx'
import RiskHistoryPage from '../pages/RiskHistoryPage.jsx'

function RootRedirect() {
  const { isAuthenticated } = useAuth()

  return <Navigate to={isAuthenticated ? '/dashboard' : '/login'} replace />
}

function PublicOnlyRoute() {
  const { isAuthenticated } = useAuth()

  if (isAuthenticated) {
    return <Navigate to="/dashboard" replace />
  }

  return <Outlet />
}

const router = createBrowserRouter(
  createRoutesFromElements(
    <>
      <Route path="/" element={<RootRedirect />} />

      <Route element={<PublicOnlyRoute />}>
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
      </Route>

      <Route element={<ProtectedRoute />}>
        <Route element={<ProtectedLayout />}>
          <Route path="/dashboard" element={<DashboardPage />} />
          <Route path="/add-vitals" element={<AddVitalsPage />} />
          <Route path="/risk-history" element={<RiskHistoryPage />} />
        </Route>
      </Route>

      <Route path="*" element={<RootRedirect />} />
    </>,
  ),
)

function AppRouter() {
  return <RouterProvider router={router} />
}

export default AppRouter
