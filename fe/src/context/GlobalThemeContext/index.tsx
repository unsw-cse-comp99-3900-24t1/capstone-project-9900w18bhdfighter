/* eslint-disable @typescript-eslint/no-explicit-any */
import { ConfigProvider, theme as _theme } from 'antd'
import type { ThemeConfig } from 'antd'
import {
  Dispatch,
  ReactNode,
  createContext,
  useContext,
  useEffect,
  useState,
} from 'react'
import { ThemeProvider } from 'styled-components'
import { ThemeColor, themeColor as _themeColor } from './themeConfig'

import breakPoint, { BreakPointKey } from '../../constant/breakPoint'

type Props = {
  children: ReactNode
}
type OnWidth = (
  bp: Partial<Record<BreakPointKey, any>> & { defaultValue: any }
) => typeof bp.defaultValue
interface GlobalThemeContextType {
  setThemeColor: Dispatch<ThemeColor>
  windowWidth: number
  onWidth: OnWidth
}

const GlobalThemeContext = createContext<GlobalThemeContextType>(
  {} as GlobalThemeContextType
)

export const useGlobalTheme = () => useContext(GlobalThemeContext)
const GlobalAntdThemeProvider = ({ children }: Props) => {
  const { token } = _theme.useToken()
  const [windowWidth, setWindowWidth] = useState(window.innerWidth)
  //when the window width is less than the breakpoint, return the value of the breakpoint
  const onWidth: OnWidth = (bp) => {
    const keysWithoutDefault = Object.keys(bp).filter(
      (k) => k !== 'defaultValue'
    ) as BreakPointKey[]

    const defaultValue = bp.defaultValue
    keysWithoutDefault.sort((a, b) => breakPoint[a] - breakPoint[b])
    for (const key of keysWithoutDefault) {
      if (windowWidth < breakPoint[key]) {
        return bp[key]
      }
    }
    return defaultValue
  }
  useEffect(() => {
    window.addEventListener('resize', () => {
      setWindowWidth(window.innerWidth)
    })
    return () => {
      window.removeEventListener('resize', () => {
        setWindowWidth(window.innerWidth)
      })
    }
  }, [])

  const [themeState] = useState<ThemeConfig>({
    components: {
      Typography: {
        titleMarginBottom: 0,
        fontWeightStrong: 700,
      },
      Layout: {
        headerBg: _themeColor.basicBg,
        siderBg: _themeColor.basicBg,
        footerBg: _themeColor.basicBg,
        triggerBg: _themeColor.highlight,
        triggerColor: _themeColor.primary,
        triggerHeight: 48,
        headerHeight: 64,
      },
      DatePicker: {
        colorBgTextActive: _themeColor.highlight,
        colorBgTextHover: _themeColor.highlight,
        colorBgBase: _themeColor.grayscalePalette[0] as string,
        colorBgSpotlight: _themeColor.highlight,
        colorFillContent: _themeColor.highlight,
      },

      Menu: {
        itemSelectedColor: _themeColor.grayscalePalette[0] as string,
      },
      Table: {
        rowSelectedBg: _themeColor.grayscalePalette[20] as string,
        rowSelectedHoverBg: _themeColor.grayscalePalette[20] as string,
      },
      Select: {
        optionSelectedBg: _themeColor.highlightSecondary,
        optionActiveBg: _themeColor.grayscalePalette[2] as string,
      },
      Button: {
        colorPrimaryHover: _themeColor.grayscalePalette[35] as string,
      },
    },
    token: {
      colorPrimary: _themeColor.primary,
      borderRadius: 0,
    },
  })
  const [themeColor, setThemeColor] = useState<ThemeColor>(_themeColor)

  const ctx = {
    setThemeColor,
    windowWidth,
    onWidth,
  }
  return (
    <GlobalThemeContext.Provider value={ctx}>
      <ThemeProvider
        theme={{ ...token, ...themeState, themeColor: themeColor }}
      >
        <ConfigProvider
          theme={{
            ..._theme,
            ...themeState,
          }}
        >
          {children}
        </ConfigProvider>
      </ThemeProvider>
    </GlobalThemeContext.Provider>
  )
}

export default GlobalAntdThemeProvider
