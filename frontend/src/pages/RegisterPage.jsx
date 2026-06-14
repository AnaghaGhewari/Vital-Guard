import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import client from '../api/client.js'
import { getApiErrorMessage } from '../utils/authErrors.js'

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
    <main>
      <h1>Register</h1>
      <p>Create your VitalGuard account.</p>

      {errorMessage ? <p role="alert">{errorMessage}</p> : null}

      <form onSubmit={handleSubmit} noValidate>
        <div>
          <label htmlFor="name">Name</label>
          <input
            id="name"
            name="name"
            type="text"
            autoComplete="name"
            value={formData.name}
            onChange={handleChange}
            disabled={isSubmitting}
          />
          {errors.name ? <p role="alert">{errors.name}</p> : null}
        </div>

        <div>
          <label htmlFor="email">Email</label>
          <input
            id="email"
            name="email"
            type="email"
            autoComplete="email"
            value={formData.email}
            onChange={handleChange}
            disabled={isSubmitting}
          />
          {errors.email ? <p role="alert">{errors.email}</p> : null}
        </div>

        <div>
          <label htmlFor="password">Password</label>
          <input
            id="password"
            name="password"
            type="password"
            autoComplete="new-password"
            value={formData.password}
            onChange={handleChange}
            disabled={isSubmitting}
          />
          {errors.password ? <p role="alert">{errors.password}</p> : null}
        </div>

        <button type="submit" disabled={isSubmitting}>
          {isSubmitting ? 'Creating account...' : 'Register'}
        </button>
      </form>

      <p>
        Already have an account? <Link to="/login">Login here</Link>.
      </p>
    </main>
  )
}

export default RegisterPage
