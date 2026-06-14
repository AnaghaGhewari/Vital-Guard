/* eslint-disable react-refresh/only-export-components */
import { createContext, useContext, useState } from 'react'
import { AUTH_TOKEN_STORAGE_KEY } from '../api/client.js'

const AuthContext = createContext(undefined)

function getStoredToken() {
  if (typeof window === 'undefined') {
    return null
  }

  return window.localStorage.getItem(AUTH_TOKEN_STORAGE_KEY)
}

export function AuthProvider({ children }) {
  const [token, setToken] = useState(getStoredToken)
  const [user, setUser] = useState(null)

  const login = (nextToken, nextUser = null) => {
    setToken(nextToken)
    setUser(nextUser)

    if (typeof window === 'undefined') {
      return
    }

    if (nextToken) {
      window.localStorage.setItem(AUTH_TOKEN_STORAGE_KEY, nextToken)
      return
    }

    window.localStorage.removeItem(AUTH_TOKEN_STORAGE_KEY)
  }

  const logout = () => {
    setToken(null)
    setUser(null)

    if (typeof window === 'undefined') {
      return
    }

    window.localStorage.removeItem(AUTH_TOKEN_STORAGE_KEY)
  }

  return (
    <AuthContext.Provider
      value={{
        token,
        user,
        isAuthenticated: Boolean(token),
        login,
        logout,
        setUser,
      }}
    >
      {children}
    </AuthContext.Provider>
  )
}

export function useAuth() {
  const authContext = useContext(AuthContext)

  if (!authContext) {
    throw new Error('useAuth must be used within an AuthProvider.')
  }

  return authContext
}
