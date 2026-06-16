import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import client from '../api/client.js'
import DashboardCard from '../components/dashboard/DashboardCard.jsx'
import DashboardStatusPanel from '../components/dashboard/DashboardStatusPanel.jsx'
import './DashboardPage.css'

function formatFeatureName(featureName) {
  return String(featureName)
    .split('_')
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(' ')
}

function formatRiskScore(riskScore) {
  return Number.isFinite(riskScore) ? riskScore.toFixed(3) : '--'
}

function formatContribution(value) {
  const numericValue = Number(value)

  if (!Number.isFinite(numericValue)) {
    return '--'
  }

  return `${numericValue >= 0 ? '+' : ''}${numericValue.toFixed(4)}`
}

function formatGeneratedAt(generatedAt) {
  const generatedDate = new Date(generatedAt)

  if (Number.isNaN(generatedDate.getTime())) {
    return 'Unavailable'
  }

  return new Intl.DateTimeFormat('en-US', {
    dateStyle: 'medium',
    timeStyle: 'short',
  }).format(generatedDate)
}

function getRiskTone(level) {
  const normalizedLevel = String(level).toLowerCase()

  if (normalizedLevel === 'high') {
    return 'high'
  }

  if (normalizedLevel === 'medium') {
    return 'medium'
  }

  if (normalizedLevel === 'low') {
    return 'low'
  }

  return 'neutral'
}

function getDashboardErrorMessage(error) {
  const detail = error?.response?.data?.detail

  if (typeof detail === 'string' && detail.trim()) {
    return detail
  }

  if (Array.isArray(detail) && detail.length > 0) {
    return detail
      .map((issue) => issue?.msg)
      .filter(Boolean)
      .join(' ')
  }

  return 'Something went wrong while loading your dashboard. Please try again.'
}

function isRiskDataAvailable(result) {
  return (
    result !== null &&
    typeof result === 'object' &&
    result.risk_score !== null &&
    result.risk_score !== undefined &&
    typeof result.level === 'string'
  )
}

async function fetchDashboardRisk(signal) {
  try {
    const response = await client.get('/api/v1/risk/score', { signal })
    const nextRiskResult = response.data

    if (!isRiskDataAvailable(nextRiskResult)) {
      return {
        dashboardStatus: 'empty',
        feedbackMessage: 'No risk prediction is available yet.',
        riskResult: null,
      }
    }

    return {
      dashboardStatus: 'success',
      feedbackMessage: '',
      riskResult: nextRiskResult,
    }
  } catch (error) {
    if (error?.code === 'ERR_CANCELED') {
      return null
    }

    if (error?.response?.status === 404) {
      return {
        dashboardStatus: 'empty',
        feedbackMessage:
          typeof error.response.data?.detail === 'string'
            ? error.response.data.detail
            : 'No vitals have been logged yet.',
        riskResult: null,
      }
    }

    return {
      dashboardStatus: 'error',
      feedbackMessage: getDashboardErrorMessage(error),
      riskResult: null,
    }
  }
}

function DashboardPage() {
  const [dashboardStatus, setDashboardStatus] = useState('loading')
  const [riskResult, setRiskResult] = useState(null)
  const [feedbackMessage, setFeedbackMessage] = useState('')

  const loadRiskResult = async (signal) => {
    setDashboardStatus('loading')
    setFeedbackMessage('')

    const nextDashboardState = await fetchDashboardRisk(signal)

    if (!nextDashboardState) {
      return
    }

    setRiskResult(nextDashboardState.riskResult)
    setDashboardStatus(nextDashboardState.dashboardStatus)
    setFeedbackMessage(nextDashboardState.feedbackMessage)
  }

  useEffect(() => {
    const abortController = new AbortController()

    const syncDashboard = async () => {
      const nextDashboardState = await fetchDashboardRisk(abortController.signal)

      if (!nextDashboardState) {
        return
      }

      setRiskResult(nextDashboardState.riskResult)
      setDashboardStatus(nextDashboardState.dashboardStatus)
      setFeedbackMessage(nextDashboardState.feedbackMessage)
    }

    syncDashboard()

    return () => {
      abortController.abort()
    }
  }, [])

  const handleRetry = () => {
    loadRiskResult()
  }

  const riskTone = getRiskTone(riskResult?.level)
  const topFactors = Array.isArray(riskResult?.top_factors)
    ? riskResult.top_factors
    : []
  const shapContributions = Object.entries(riskResult?.shap_explanation ?? {}).sort(
    (leftEntry, rightEntry) => Math.abs(rightEntry[1]) - Math.abs(leftEntry[1]),
  )

  return (
    <main className="dashboard-page">
      <section className="dashboard-page__hero">
        <div className="dashboard-page__hero-copy">
          <p className="dashboard-page__eyebrow">AI Health Monitoring</p>
          <h1 className="dashboard-page__title">Your Risk Dashboard</h1>
          <p className="dashboard-page__lead">
            Review your latest diabetes risk prediction, the factors driving it,
            and the explanation generated from your most recent vital record.
          </p>
        </div>

        {dashboardStatus === 'success' ? (
          <div className={`dashboard-page__hero-badge dashboard-page__hero-badge--${riskTone}`}>
            Latest prediction ready
          </div>
        ) : null}
      </section>

      {dashboardStatus === 'loading' ? (
        <DashboardStatusPanel
          tone="loading"
          title="Loading your latest prediction"
          message="We are fetching the newest AI risk assessment from your VitalGuard account."
        />
      ) : null}

      {dashboardStatus === 'error' ? (
        <DashboardStatusPanel
          tone="error"
          title="We could not load your dashboard"
          message={feedbackMessage}
          actionLabel="Try Again"
          onAction={handleRetry}
        />
      ) : null}

      {dashboardStatus === 'empty' ? (
        <DashboardStatusPanel
          tone="empty"
          title="No risk data yet"
          message={feedbackMessage}
          supportMessage="Add a set of vitals to generate your first AI-powered risk assessment."
          actionLabel="Add Vitals"
          actionTo="/add-vitals"
        />
      ) : null}

      {dashboardStatus === 'success' && riskResult ? (
        <section className="dashboard-grid" aria-label="Risk dashboard cards">
          <DashboardCard
            className="dashboard-card--overview"
            title="Risk Score"
            subtitle="Latest prediction from your current health snapshot"
          >
            <div className="risk-overview">
              <div>
                <p className="risk-overview__value">
                  {formatRiskScore(riskResult.risk_score)}
                </p>
                <p className="risk-overview__caption">Predicted risk score</p>
              </div>

              <div className={`risk-level-pill risk-level-pill--${riskTone}`}>
                {String(riskResult.level).toUpperCase()}
              </div>
            </div>
          </DashboardCard>

          <DashboardCard
            className="dashboard-card--factors"
            title="Top Risk Factors"
            subtitle="Highest-impact signals in this prediction"
          >
            {topFactors.length > 0 ? (
              <div className="factor-badges">
                {topFactors.map((factor) => (
                  <span key={factor} className="factor-badge">
                    {formatFeatureName(factor)}
                  </span>
                ))}
              </div>
            ) : (
              <p className="dashboard-card__empty">
                No top risk factors were returned for this result.
              </p>
            )}
          </DashboardCard>

          <DashboardCard
            className="dashboard-card--metadata"
            title="Metadata"
            subtitle="When this prediction was generated"
          >
            <div className="metadata-block">
              <p className="metadata-block__label">Generated At</p>
              <p className="metadata-block__value">
                {formatGeneratedAt(riskResult.generated_at)}
              </p>
            </div>
          </DashboardCard>

          <DashboardCard
            className="dashboard-card--shap"
            title="SHAP Feature Contributions"
            subtitle="Positive values increase risk while negative values reduce it"
          >
            {shapContributions.length > 0 ? (
              <div className="contribution-list">
                {shapContributions.map(([featureName, contribution]) => (
                  <div key={featureName} className="contribution-row">
                    <div className="contribution-row__label-group">
                      <p className="contribution-row__feature">
                        {formatFeatureName(featureName)}
                      </p>
                      <p className="contribution-row__meta">Feature contribution</p>
                    </div>
                    <p
                      className={`contribution-row__value ${
                        contribution >= 0
                          ? 'contribution-row__value--positive'
                          : 'contribution-row__value--negative'
                      }`}
                    >
                      {formatContribution(contribution)}
                    </p>
                  </div>
                ))}
              </div>
            ) : (
              <p className="dashboard-card__empty">
                SHAP feature contributions are not available for this result.
              </p>
            )}
          </DashboardCard>

          <DashboardCard
            className="dashboard-card--explanation"
            title="AI Explanation"
            subtitle="Readable summary of what is driving your prediction"
          >
            <p className="explanation-card__text">
              {riskResult.explanation || 'No explanation was provided for this result.'}
            </p>
            <p className="explanation-card__link-row">
              Need to improve this forecast? <Link to="/add-vitals">Log fresh vitals</Link>.
            </p>
          </DashboardCard>
        </section>
      ) : null}
    </main>
  )
}

export default DashboardPage
