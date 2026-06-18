import { useState } from 'react'
import { Link, useLocation, useNavigate } from 'react-router-dom'
import client from '../api/client.js'
import { useAuth } from '../context/AuthContext.jsx'
import { getApiErrorMessage } from '../utils/authErrors.js'
import './LoginPage.css'

function validateLoginForm(formData) {
  const errors = {}

  if (!formData.email.trim()) {
    errors.email = 'Email is required.'
  }

  if (!formData.password.trim()) {
    errors.password = 'Password is required.'
  }

  return errors
}

function LoginPage() {
  const navigate = useNavigate()
  const location = useLocation()
  const { login } = useAuth()
  const successMessage =
    typeof location.state?.message === 'string' ? location.state.message : ''
  const [formData, setFormData] = useState({
    email: typeof location.state?.email === 'string' ? location.state.email : '',
    password: '',
  })
  const [errors, setErrors] = useState({})
  const [errorMessage, setErrorMessage] = useState('')
  const [isSubmitting, setIsSubmitting] = useState(false)

  const handleChange = (event) => {
    const { name, value } = event.target

    setFormData((currentFormData) => ({
      ...currentFormData,
      [name]: value,
    }))
    setErrors((currentErrors) => ({
      ...currentErrors,
      [name]: '',
    }))
    setErrorMessage('')
  }

  const handleSubmit = async (event) => {
    event.preventDefault()

    const validationErrors = validateLoginForm(formData)
    setErrors(validationErrors)
    setErrorMessage('')

    if (Object.keys(validationErrors).length > 0) {
      return
    }

    setIsSubmitting(true)

    try {
      const formBody = new URLSearchParams()
      formBody.set('username', formData.email.trim())
      formBody.set('password', formData.password)

      const response = await client.post('/api/v1/auth/login', formBody, {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
      })

      login(response.data.access_token, { id: response.data.user_id })

      navigate(location.state?.from?.pathname ?? '/dashboard', {
        replace: true,
      })
    } catch (error) {
      setErrorMessage(
        getApiErrorMessage(
          error,
          'Unable to log in right now. Please check your credentials and try again.',
        ),
      )
    } finally {
      setIsSubmitting(false)
    }
  }

  return (
  <main className="login-page">
    <section className="login-card">
      <div className="login-brand">
        <p className="login-brand__eyebrow">
          AI Health Monitoring
        </p>

        <h1 className="login-brand__title">
          VitalGuard
        </h1>

        <p className="login-brand__subtitle">
          Sign in to access your health dashboard,
          risk predictions and monitoring history.
        </p>
      </div>

      {successMessage ? (
        <div className="login-success">
          {successMessage}
        </div>
      ) : null}

      {errorMessage ? (
        <div className="login-error" role="alert">
          {errorMessage}
        </div>
      ) : null}

      <form
        className="login-form"
        onSubmit={handleSubmit}
        noValidate
      >
        <div className="login-field">
          <label htmlFor="email">Email Address</label>

          <input
            id="email"
            name="email"
            type="email"
            autoComplete="email"
            value={formData.email}
            onChange={handleChange}
            disabled={isSubmitting}
            placeholder="Enter your email"
          />

          {errors.email ? (
            <p className="login-validation">
              {errors.email}
            </p>
          ) : null}
        </div>

        <div className="login-field">
          <label htmlFor="password">Password</label>

          <input
            id="password"
            name="password"
            type="password"
            autoComplete="current-password"
            value={formData.password}
            onChange={handleChange}
            disabled={isSubmitting}
            placeholder="Enter your password"
          />

          {errors.password ? (
            <p className="login-validation">
              {errors.password}
            </p>
          ) : null}
        </div>

        <button
          className="login-button"
          type="submit"
          disabled={isSubmitting}
        >
          {isSubmitting ? 'Signing In...' : 'Sign In'}
        </button>
      </form>

      <div className="login-footer">
        Need an account?{' '}
        <Link to="/register">
          Create one here
        </Link>
      </div>
    </section>
  </main>
)
}

export default LoginPage
