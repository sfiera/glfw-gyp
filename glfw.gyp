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
      , "glfw-3.1.1/src/cocoa_init.m"
      , "glfw-3.1.1/src/cocoa_monitor.m"
      , "glfw-3.1.1/src/cocoa_window.m"
      , "glfw-3.1.1/src/iokit_joystick.m"
      , "glfw-3.1.1/src/mach_time.c"
      , "glfw-3.1.1/src/posix_tls.c"
      , "glfw-3.1.1/src/nsgl_context.m"
      ]
    , "defines": ["_GLFW_USE_CONFIG_H"]
    , "include_dirs":
      [ "glfw-3.1.1/src"
      , "glfw-3.1.1/include"
      , "src/mac"
      ]
    , "direct_dependent_settings":
      { "include_dirs": [ "glfw-3.1.1/include" ]
      }
    , "link_settings":
      { "libraries":
        [ "$(SDKROOT)/System/Library/Frameworks/Cocoa.framework"
        , "$(SDKROOT)/System/Library/Frameworks/CoreVideo.framework"
        , "$(SDKROOT)/System/Library/Frameworks/IOKit.framework"
        , "$(SDKROOT)/System/Library/Frameworks/OpenGL.framework"
        ]
      }
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
