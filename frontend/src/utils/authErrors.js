export function getApiErrorMessage(error, fallbackMessage) {
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

  return fallbackMessage
}
