import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import client from '../api/client.js'
import { getApiErrorMessage } from '../utils/authErrors.js'
import './RegisterPage.css'

function validateRegisterForm(formData) {
  const errors = {}

  if (!formData.name.trim()) {
    errors.name = 'Name is required.'
  }

  if (!formData.email.trim()) {
    errors.email = 'Email is required.'
  }

  if (!formData.password.trim()) {
    errors.password = 'Password is required.'
  }

  return errors
}

function RegisterPage() {
  const navigate = useNavigate()
  const [formData, setFormData] = useState({
    name: '',
    email: '',
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

    const validationErrors = validateRegisterForm(formData)
    setErrors(validationErrors)
    setErrorMessage('')

    if (Object.keys(validationErrors).length > 0) {
      return
    }

    setIsSubmitting(true)

    try {
      await client.post('/api/v1/auth/register', {
        name: formData.name.trim(),
        email: formData.email.trim(),
        password: formData.password,
      })

      navigate('/login', {
        replace: true,
        state: {
          email: formData.email.trim(),
          message: 'Registration successful. Please log in to continue.',
        },
      })
    } catch (error) {
      setErrorMessage(
        getApiErrorMessage(
          error,
          'Unable to create your account right now. Please try again.',
        ),
      )
    } finally {
      setIsSubmitting(false)
    }
  }

  return (
  <main className="register-page">
    <section className="register-card">
      <div className="register-brand">
        <p className="register-brand__eyebrow">
          AI Health Monitoring
        </p>

        <h1 className="register-brand__title">
          VitalGuard
        </h1>

        <p className="register-brand__subtitle">
          Create your account and start tracking your health with AI-powered insights and personalized risk monitoring.
        </p>
      </div>

      {errorMessage ? (
        <div className="register-error" role="alert">
          {errorMessage}
        </div>
      ) : null}

      <form
        className="register-form"
        onSubmit={handleSubmit}
        noValidate
      >
        <div className="register-field">
          <label htmlFor="name">Full Name</label>

          <input
            id="name"
            name="name"
            type="text"
            autoComplete="name"
            value={formData.name}
            onChange={handleChange}
            disabled={isSubmitting}
            placeholder="Enter your full name"
          />

          {errors.name ? (
            <p className="register-validation">
              {errors.name}
            </p>
          ) : null}
        </div>

        <div className="register-field">
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
            <p className="register-validation">
              {errors.email}
            </p>
          ) : null}
        </div>

        <div className="register-field">
          <label htmlFor="password">Password</label>

          <input
            id="password"
            name="password"
            type="password"
            autoComplete="new-password"
            value={formData.password}
            onChange={handleChange}
            disabled={isSubmitting}
            placeholder="Create a password"
          />

          {errors.password ? (
            <p className="register-validation">
              {errors.password}
            </p>
          ) : null}
        </div>

        <button
          className="register-button"
          type="submit"
          disabled={isSubmitting}
        >
          {isSubmitting ? 'Creating Account...' : 'Create Account'}
        </button>
      </form>

      <div className="register-footer">
        Already have an account?{' '}
        <Link to="/login">
          Sign in here
        </Link>
      </div>
    </section>
  </main>
)
}

export default RegisterPage
