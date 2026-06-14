/* eslint-disable react-refresh/only-export-components */
import { createContext, useContext, useState } from 'react'
import {
  AUTH_TOKEN_STORAGE_KEY,
  AUTH_USER_ID_STORAGE_KEY,
} from '../api/client.js'

const AuthContext = createContext(undefined)

function getStoredAuthState() {
  if (typeof window === 'undefined') {
    return {
      token: null,
      user: null,
    }
  }

  const token = window.localStorage.getItem(AUTH_TOKEN_STORAGE_KEY)
  const storedUserId = window.localStorage.getItem(AUTH_USER_ID_STORAGE_KEY)
  const parsedUserId = storedUserId ? Number(storedUserId) : null

  return {
    token,
    user:
      Number.isFinite(parsedUserId) && parsedUserId !== null
        ? { id: parsedUserId }
        : null,
  }
}

export function AuthProvider({ children }) {
  const [authState, setAuthState] = useState(getStoredAuthState)
  const { token, user } = authState

  const login = (nextToken, nextUser = null) => {
    setAuthState({
      token: nextToken,
      user: nextUser,
    })

    if (typeof window === 'undefined') {
      return
    }

    if (nextToken) {
      window.localStorage.setItem(AUTH_TOKEN_STORAGE_KEY, nextToken)
    } else {
      window.localStorage.removeItem(AUTH_TOKEN_STORAGE_KEY)
    }

    if (nextUser?.id) {
      window.localStorage.setItem(
        AUTH_USER_ID_STORAGE_KEY,
        String(nextUser.id),
      )
      return
    }

    window.localStorage.removeItem(AUTH_USER_ID_STORAGE_KEY)
  }

  const logout = () => {
    setAuthState({
      token: null,
      user: null,
    })
  }

  const updateUser = (nextUser) => {
    setAuthState((currentAuthState) => ({
      ...currentAuthState,
      user: nextUser,
    }))

    if (typeof window === 'undefined') {
      return
    }

    if (nextUser?.id) {
      window.localStorage.setItem(
        AUTH_USER_ID_STORAGE_KEY,
        String(nextUser.id),
      )
      return
    }

    window.localStorage.removeItem(AUTH_USER_ID_STORAGE_KEY)
  }

  const clearStoredAuth = () => {
    if (typeof window === 'undefined') {
      return
    }

    window.localStorage.removeItem(AUTH_TOKEN_STORAGE_KEY)
    window.localStorage.removeItem(AUTH_USER_ID_STORAGE_KEY)
  }

  return (
    <AuthContext.Provider
      value={{
        token,
        user,
        userId: user?.id ?? null,
        isAuthenticated: Boolean(token),
        login,
        logout: () => {
          logout()
          clearStoredAuth()
        },
        setUser: updateUser,
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
