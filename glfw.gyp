{ "target_defaults":
  { "cflags":
    [ "-Wall"
    , "-Wno-deprecated-declarations"
    ]
  , "xcode_settings":
    { "WARNING_CFLAGS":
      [ "-Wall"
      , "-Wno-deprecated-declarations"
      ]
    }
  }
, "targets":
  [ { "target_name": "libglfw"
    , "product_prefix": ""
    , "type": "static_library"
    , "sources":
      [ "glfw-3.1.1/src/context.c"
      , "glfw-3.1.1/src/init.c"
      , "glfw-3.1.1/src/input.c"
      , "glfw-3.1.1/src/monitor.c"
      , "glfw-3.1.1/src/window.c"
      ]
    , "defines": ["_GLFW_USE_CONFIG_H"]
    , "include_dirs":
      [ "glfw-3.1.1/src"
      , "glfw-3.1.1/include"
      ]
    , "direct_dependent_settings":
      { "include_dirs": [ "glfw-3.1.1/include" ]
      }
    , "conditions":
      [ [ "OS == 'mac'"
        , { "sources":
            [ "glfw-3.1.1/src/cocoa_init.m"
            , "glfw-3.1.1/src/cocoa_monitor.m"
            , "glfw-3.1.1/src/cocoa_window.m"
            , "glfw-3.1.1/src/iokit_joystick.m"
            , "glfw-3.1.1/src/mach_time.c"
            , "glfw-3.1.1/src/posix_tls.c"
            , "glfw-3.1.1/src/nsgl_context.m"
            ]
          , "include_dirs": [ "src/mac" ]
          , "link_settings":
            { "libraries":
              [ "$(SDKROOT)/System/Library/Frameworks/Cocoa.framework"
              , "$(SDKROOT)/System/Library/Frameworks/CoreVideo.framework"
              , "$(SDKROOT)/System/Library/Frameworks/IOKit.framework"
              , "$(SDKROOT)/System/Library/Frameworks/OpenGL.framework"
              ]
            }
          }
        ]
      , [ "OS == 'linux'"
        , { "sources":
            [ "glfw-3.1.1/src/x11_init.c"
            , "glfw-3.1.1/src/x11_monitor.c"
            , "glfw-3.1.1/src/x11_window.c"
            , "glfw-3.1.1/src/xkb_unicode.c"
            , "glfw-3.1.1/src/linux_joystick.c"
            , "glfw-3.1.1/src/posix_time.c"
            , "glfw-3.1.1/src/posix_tls.c"
            , "glfw-3.1.1/src/glx_context.c"
            ]
          , "include_dirs": [ "src/linux" ]
          , "link_settings":
            { "libraries":
              [ "-lGL"
              , "-lGLU"
              , "-lm"
              , "-lpthread"
              , "-lX11"
              , "-lXcursor"
              , "-lXinerama"
              , "-lXxf86vm"
              , "-lXrandr"
              ]
            }
          }
        ]
      ]
    }

  , { "target_name": "boing"
    , "type": "executable"
    , "sources": [ "glfw-3.1.1/examples/boing.c" ]
    , "dependencies": ["libglfw"]
    }

  , { "target_name": "gears"
    , "type": "executable"
    , "sources": [ "glfw-3.1.1/examples/gears.c" ]
    , "dependencies": ["libglfw"]
    }

  , { "target_name": "wave"
    , "type": "executable"
    , "sources": [ "glfw-3.1.1/examples/wave.c" ]
    , "dependencies": ["libglfw"]
    }
  ]
}
# -*- mode: python; tab-width: 2 -*-
