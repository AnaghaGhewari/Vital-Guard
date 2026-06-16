import { Link } from 'react-router-dom'

function DashboardStatusPanel({
  tone = 'neutral',
  title,
  message,
  supportMessage = '',
  actionLabel = '',
  actionTo = '',
  onAction,
}) {
  const role = tone === 'error' ? 'alert' : 'status'

  return (
    <section className={`dashboard-status dashboard-status--${tone}`} role={role}>
      <p className="dashboard-status__eyebrow">Dashboard Status</p>
      <h2 className="dashboard-status__title">{title}</h2>
      <p className="dashboard-status__message">{message}</p>
      {supportMessage ? (
        <p className="dashboard-status__support">{supportMessage}</p>
      ) : null}

      {actionTo && actionLabel ? (
        <Link className="dashboard-status__action" to={actionTo}>
          {actionLabel}
        </Link>
      ) : null}

      {!actionTo && actionLabel && onAction ? (
        <button
          className="dashboard-status__action"
          type="button"
          onClick={onAction}
        >
          {actionLabel}
        </button>
      ) : null}
    </section>
  )
}

export default DashboardStatusPanel
