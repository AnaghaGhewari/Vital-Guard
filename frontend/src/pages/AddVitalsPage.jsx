import { useState } from 'react'
import { Link } from 'react-router-dom'
import client from '../api/client.js'
import DashboardCard from '../components/dashboard/DashboardCard.jsx'
import DashboardStatusPanel from '../components/dashboard/DashboardStatusPanel.jsx'
import { getApiErrorMessage } from '../utils/authErrors.js'
import './DashboardPage.css'
import './AddVitalsPage.css'

const INITIAL_FORM_DATA = {
  heart_rate: '',
  sleep_hours: '',
  steps: '',
  glucose: '',
  blood_pressure: '',
  bmi: '',
  age: '',
  notes: '',
}

const DAILY_METRICS_FIELDS = [
  {
    name: 'heart_rate',
    label: 'Heart Rate',
    type: 'number',
    min: '30',
    max: '220',
    step: '1',
    placeholder: 'e.g. 72',
    helperText: 'Required. Enter a value between 30 and 220 BPM.',
  },
  {
    name: 'sleep_hours',
    label: 'Sleep Hours',
    type: 'number',
    min: '0',
    max: '24',
    step: '0.1',
    placeholder: 'e.g. 7.5',
    helperText: 'Required. Enter total sleep between 0 and 24 hours.',
  },
  {
    name: 'steps',
    label: 'Steps',
    type: 'number',
    min: '0',
    step: '1',
    placeholder: 'e.g. 6500',
    helperText: "Required. Enter today's step count.",
  },
]

const RISK_INPUT_FIELDS = [
  {
    name: 'glucose',
    label: 'Glucose',
    type: 'number',
    min: '0',
    max: '300',
    step: '0.1',
    placeholder: 'e.g. 120',
    helperText: 'Optional. Range: 0 to 300 mg/dL.',
  },
  {
    name: 'blood_pressure',
    label: 'Blood Pressure',
    type: 'number',
    min: '0',
    max: '200',
    step: '0.1',
    placeholder: 'e.g. 80',
    helperText: 'Optional. Range: 0 to 200 mmHg.',
  },
  {
    name: 'bmi',
    label: 'BMI',
    type: 'number',
    min: '0',
    max: '80',
    step: '0.1',
    placeholder: 'e.g. 24.0',
    helperText: 'Optional. Range: 0 to 80.',
  },
  {
    name: 'age',
    label: 'Age',
    type: 'number',
    min: '1',
    max: '120',
    step: '0.1',
    placeholder: 'e.g. 25',
    helperText: 'Optional. Range: 1 to 120 years.',
  },
]

function parseInteger(value) {
  if (!/^-?\d+$/.test(value.trim())) {
    return Number.NaN
  }

  return Number.parseInt(value, 10)
}

function parseDecimal(value) {
  const parsedValue = Number(value)
  return Number.isFinite(parsedValue) ? parsedValue : Number.NaN
}

function validateRequiredIntegerField(errors, formData, fieldName, label, min, max) {
  const rawValue = formData[fieldName].trim()

  if (!rawValue) {
    errors[fieldName] = `${label} is required.`
    return
  }

  const numericValue = parseInteger(rawValue)

  if (!Number.isInteger(numericValue)) {
    errors[fieldName] = `${label} must be a whole number.`
    return
  }

  if (numericValue < min || numericValue > max) {
    errors[fieldName] = `${label} must be between ${min} and ${max}.`
  }
}

function validateRequiredDecimalField(errors, formData, fieldName, label, min, max) {
  const rawValue = formData[fieldName].trim()

  if (!rawValue) {
    errors[fieldName] = `${label} is required.`
    return
  }

  const numericValue = parseDecimal(rawValue)

  if (!Number.isFinite(numericValue)) {
    errors[fieldName] = `${label} must be a valid number.`
    return
  }

  if (numericValue < min || numericValue > max) {
    errors[fieldName] = `${label} must be between ${min} and ${max}.`
  }
}

function validateOptionalDecimalField(errors, formData, fieldName, label, min, max) {
  const rawValue = formData[fieldName].trim()

  if (!rawValue) {
    return
  }

  const numericValue = parseDecimal(rawValue)

  if (!Number.isFinite(numericValue)) {
    errors[fieldName] = `${label} must be a valid number.`
    return
  }

  if (numericValue < min || numericValue > max) {
    errors[fieldName] = `${label} must be between ${min} and ${max}.`
  }
}

function validateNotesField(errors, formData) {
  const noteLength = formData.notes.trim().length

  if (noteLength > 300) {
    errors.notes = 'Notes cannot exceed 300 characters.'
  }
}

function validateVitalsForm(formData) {
  const errors = {}

  validateRequiredIntegerField(
    errors,
    formData,
    'heart_rate',
    'Heart rate',
    30,
    220,
  )
  validateRequiredDecimalField(
    errors,
    formData,
    'sleep_hours',
    'Sleep hours',
    0,
    24,
  )
  validateRequiredIntegerField(errors, formData, 'steps', 'Steps', 0, Number.MAX_SAFE_INTEGER)

  validateOptionalDecimalField(errors, formData, 'glucose', 'Glucose', 0, 300)
  validateOptionalDecimalField(
    errors,
    formData,
    'blood_pressure',
    'Blood pressure',
    0,
    200,
  )
  validateOptionalDecimalField(errors, formData, 'bmi', 'BMI', 0, 80)
  validateOptionalDecimalField(errors, formData, 'age', 'Age', 1, 120)
  validateNotesField(errors, formData)

  return errors
}

function mapServerFieldErrors(error) {
  const detail = error?.response?.data?.detail

  if (!Array.isArray(detail)) {
    return {}
  }

  return detail.reduce((fieldErrors, issue) => {
    const location = Array.isArray(issue?.loc) ? issue.loc : []
    const fieldName = location[location.length - 1]

    if (typeof fieldName === 'string' && typeof issue?.msg === 'string') {
      fieldErrors[fieldName] = issue.msg
    }

    return fieldErrors
  }, {})
}

function buildPayload(formData) {
  const payload = {
    heart_rate: parseInteger(formData.heart_rate.trim()),
    sleep_hours: parseDecimal(formData.sleep_hours.trim()),
    steps: parseInteger(formData.steps.trim()),
  }

  if (formData.glucose.trim()) {
    payload.glucose = parseDecimal(formData.glucose.trim())
  }

  if (formData.blood_pressure.trim()) {
    payload.blood_pressure = parseDecimal(formData.blood_pressure.trim())
  }

  if (formData.bmi.trim()) {
    payload.bmi = parseDecimal(formData.bmi.trim())
  }

  if (formData.age.trim()) {
    payload.age = parseDecimal(formData.age.trim())
  }

  if (formData.notes.trim()) {
    payload.notes = formData.notes.trim()
  }

  return payload
}

function formatSavedTimestamp(timestamp) {
  const savedDate = new Date(timestamp)

  if (Number.isNaN(savedDate.getTime())) {
    return 'Moments ago'
  }

  return new Intl.DateTimeFormat('en-US', {
    dateStyle: 'medium',
    timeStyle: 'short',
  }).format(savedDate)
}

function AddVitalsPage() {
  const [formData, setFormData] = useState(INITIAL_FORM_DATA)
  const [fieldErrors, setFieldErrors] = useState({})
  const [apiError, setApiError] = useState('')
  const [successState, setSuccessState] = useState(null)
  const [isSubmitting, setIsSubmitting] = useState(false)

  const handleInputChange = (event) => {
    const { name, value } = event.target

    setFormData((currentFormData) => ({
      ...currentFormData,
      [name]: value,
    }))
    setFieldErrors((currentErrors) => ({
      ...currentErrors,
      [name]: '',
    }))
    setApiError('')
    setSuccessState(null)
  }

  const handleSubmit = async (event) => {
    event.preventDefault()

    const validationErrors = validateVitalsForm(formData)
    setFieldErrors(validationErrors)
    setApiError('')
    setSuccessState(null)

    if (Object.keys(validationErrors).length > 0) {
      return
    }

    setIsSubmitting(true)

    try {
      const response = await client.post('/api/v1/vitals', buildPayload(formData))

      setFormData(INITIAL_FORM_DATA)
      setFieldErrors({})
      setSuccessState({
        id: response.data?.id ?? null,
        loggedAt: response.data?.logged_at ?? '',
      })
    } catch (error) {
      const nextFieldErrors = mapServerFieldErrors(error)

      if (Object.keys(nextFieldErrors).length > 0) {
        setFieldErrors(nextFieldErrors)
      }

      setApiError(
        Object.keys(nextFieldErrors).length > 0
          ? 'Please review the highlighted fields and try again.'
          : getApiErrorMessage(
              error,
              'We could not save your vitals right now. Please try again.',
            ),
      )
    } finally {
      setIsSubmitting(false)
    }
  }

  const renderInputField = (field) => (
    <label key={field.name} className="vitals-field">
      <span className="vitals-field__label">{field.label}</span>
      <input
        className={`vitals-field__input ${
          fieldErrors[field.name] ? 'vitals-field__input--error' : ''
        }`}
        name={field.name}
        type={field.type}
        min={field.min}
        max={field.max}
        step={field.step}
        placeholder={field.placeholder}
        value={formData[field.name]}
        onChange={handleInputChange}
        disabled={isSubmitting}
      />
      <span className="vitals-field__helper">{field.helperText}</span>
      {fieldErrors[field.name] ? (
        <span className="vitals-field__error" role="alert">
          {fieldErrors[field.name]}
        </span>
      ) : null}
    </label>
  )

  return (
    <main className="add-vitals-page">
      <section className="add-vitals-page__hero">
        <div className="add-vitals-page__hero-copy">
          <p className="add-vitals-page__eyebrow">Daily Health Logging</p>
          <h1 className="add-vitals-page__title">Add Today&apos;s Vitals</h1>
          <p className="add-vitals-page__lead">
            Save your daily health metrics and optional risk inputs so VitalGuard
            can keep your predictions current and more informative.
          </p>
        </div>

        <div className="add-vitals-page__hero-actions">
          <Link className="add-vitals-page__secondary-action" to="/dashboard">
            View Dashboard
          </Link>
        </div>
      </section>

      {apiError ? (
        <DashboardStatusPanel
          tone="error"
          title="We could not save your vitals"
          message={apiError}
        />
      ) : null}

      {successState ? (
        <DashboardStatusPanel
          tone="success"
          title="Vitals saved successfully"
          message="Your new daily health record has been sent to VitalGuard."
          supportMessage={`Saved ${successState.id ? `as record #${successState.id} ` : ''}on ${formatSavedTimestamp(successState.loggedAt)}.`}
          actionLabel="View Dashboard"
          actionTo="/dashboard"
        />
      ) : null}

      <form className="add-vitals-form" onSubmit={handleSubmit} noValidate>
        <section className="add-vitals-grid">
          <DashboardCard
            className="add-vitals-card add-vitals-card--metrics"
            title="Daily Health Metrics"
            subtitle="These core fields are required for every vital log."
          >
            <div className="vitals-field-grid vitals-field-grid--three-column">
              {DAILY_METRICS_FIELDS.map(renderInputField)}
            </div>
          </DashboardCard>

          <DashboardCard
            className="add-vitals-card add-vitals-card--inputs"
            title="Risk Prediction Inputs"
            subtitle="Optional clinical details can help power richer risk insights."
          >
            <div className="vitals-field-grid vitals-field-grid--two-column">
              {RISK_INPUT_FIELDS.map(renderInputField)}
            </div>
          </DashboardCard>

          <DashboardCard
            className="add-vitals-card add-vitals-card--notes"
            title="Notes"
            subtitle="Capture anything relevant about today's health, activity, or symptoms."
          >
            <label className="vitals-field vitals-field--full">
              <span className="vitals-field__label">Notes</span>
              <textarea
                className={`vitals-field__textarea ${
                  fieldErrors.notes ? 'vitals-field__textarea--error' : ''
                }`}
                name="notes"
                rows="6"
                maxLength="300"
                placeholder="e.g. Feeling good after a morning walk, slept deeply, no unusual symptoms."
                value={formData.notes}
                onChange={handleInputChange}
                disabled={isSubmitting}
              />
              <span className="vitals-field__helper">
                Optional. Up to 300 characters.
              </span>
              <span className="vitals-field__counter">
                {formData.notes.length}/300
              </span>
              {fieldErrors.notes ? (
                <span className="vitals-field__error" role="alert">
                  {fieldErrors.notes}
                </span>
              ) : null}
            </label>
          </DashboardCard>
        </section>

        <div className="add-vitals-form__actions">
          <button
            className="add-vitals-form__submit"
            type="submit"
            disabled={isSubmitting}
          >
            {isSubmitting ? 'Saving Vitals...' : 'Save Vitals'}
          </button>

          <Link className="add-vitals-form__dashboard-link" to="/dashboard">
            View Dashboard
          </Link>
        </div>
      </form>
    </main>
  )
}

export default AddVitalsPage
