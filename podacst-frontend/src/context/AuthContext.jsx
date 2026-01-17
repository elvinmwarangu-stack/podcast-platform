import { createContext, useContext, useState, useEffect } from 'react';
import { authApi } from '../api/auth';
import { usersApi } from '../api/users';

const AuthContext = createContext();

export const useAuth = () => useContext(AuthContext);

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) {
      usersApi.getMe()
        .then((userData) => {
          setUser(userData);
        })
        .catch((err) => {
          console.error('Auth error:', err);
          localStorage.removeItem('token');
        })
        .finally(() => setLoading(false));
    } else {
      setLoading(false);
    }
  }, []);

  const login = async (username, password) => {
    const data = await authApi.login(username, password);
    localStorage.setItem('token', data.access_token);
    const userData = await usersApi.getMe();
    setUser(userData);
  };

  const register = async (userData) => {
    await authApi.register(userData);
    await login(userData.username, userData.password);
  };

  const logout = () => {
    localStorage.removeItem('token');
    setUser(null);
  };

  const updateUser = (userData) => {
    setUser(userData);
  };

  return (
    <AuthContext.Provider value={{ user, login, register, logout, updateUser, loading }}>
      {!loading && children}
    </AuthContext.Provider>
  );
};
