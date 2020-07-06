ifeq ($(TARGET_OS),linux)

LIBGLFW3_CPPFLAGS := $(shell pkg-config --cflags glfw3)
LIBGLFW3_LDFLAGS := $(shell pkg-config --libs glfw3)

else

LIBGLFW3_CPPFLAGS := \
	-I $(GLFW_ROOT)/glfw-3.1.1/include
LIBGLFW3_LDFLAGS :=

LIBGLFW3_A := $(OUT)/libglfw3.a
LIBGLFW3_C_SRCS := \
	$(GLFW_ROOT)/glfw-3.1.1/src/context.c \
	$(GLFW_ROOT)/glfw-3.1.1/src/init.c \
	$(GLFW_ROOT)/glfw-3.1.1/src/input.c \
	$(GLFW_ROOT)/glfw-3.1.1/src/monitor.c \
	$(GLFW_ROOT)/glfw-3.1.1/src/window.c

ifeq ($(TARGET_OS),mac)
LIBGLFW3_C_SRCS += \
	$(GLFW_ROOT)/glfw-3.1.1/src/mach_time.c \
	$(GLFW_ROOT)/glfw-3.1.1/src/posix_tls.c
LIBGLFW3_M_SRCS := \
	$(GLFW_ROOT)/glfw-3.1.1/src/cocoa_init.m \
	$(GLFW_ROOT)/glfw-3.1.1/src/cocoa_monitor.m \
	$(GLFW_ROOT)/glfw-3.1.1/src/cocoa_window.m \
	$(GLFW_ROOT)/glfw-3.1.1/src/iokit_joystick.m \
	$(GLFW_ROOT)/glfw-3.1.1/src/nsgl_context.m
LIBGLFW3_LDFLAGS += \
	-framework Cocoa \
	-framework CoreVideo \
	-framework IOKit \
	-framework OpenGL
endif
ifeq ($(TARGET_OS),linux)
LIBGLFW3_C_SRCS += \
	$(GLFW_ROOT)/glfw-3.1.1/src/glx_context.c \
	$(GLFW_ROOT)/glfw-3.1.1/src/linux_joystick.c \
	$(GLFW_ROOT)/glfw-3.1.1/src/posix_time.c \
	$(GLFW_ROOT)/glfw-3.1.1/src/posix_tls.c \
	$(GLFW_ROOT)/glfw-3.1.1/src/x11_init.c \
	$(GLFW_ROOT)/glfw-3.1.1/src/x11_monitor.c \
	$(GLFW_ROOT)/glfw-3.1.1/src/x11_window.c \
	$(GLFW_ROOT)/glfw-3.1.1/src/xkb_unicode.c
LIBGLFW_LDFLAGS += \
	-lGL \
	-lGLU \
	-lm \
	-lpthread \
	-lX11 \
	-lXcursor \
	-lXinerama \
	-lXxf86vm \
	-lXrandr
endif

LIBGLFW3_C_OBJS := $(LIBGLFW3_C_SRCS:%=$(OUT)/%.o)
LIBGLFW3_M_OBJS := $(LIBGLFW3_M_SRCS:%=$(OUT)/%.o)
LIBGLFW3_OBJS := $(LIBGLFW3_C_OBJS) $(LIBGLFW3_M_OBJS)

$(LIBGLFW3_A): $(LIBGLFW3_OBJS)
	$(AR) rcs $@ $+

LIBGLFW3_PRIVATE_CPPFLAGS := \
	$(LIBGLFW3_CPPFLAGS) \
	-I $(GLFW_ROOT)/src/$(TARGET_OS) \
	-I $(GLFW_ROOT)/glfw-3.1.1/src \
	-I $(GLFW_ROOT)/glfw-3.1.1/include \
	-D _GLFW_USE_CONFIG_H  \
	-Wall \
	-Wno-deprecated-declarations

$(LIBGLFW3_C_OBJS): $(OUT)/%.c.o: %.c
	@$(MKDIR_P) $(dir $@)
	$(CC) $(CPPFLAGS) $(CFLAGS) $(LIBGLFW3_PRIVATE_CPPFLAGS) -c $< -o $@
$(LIBGLFW3_M_OBJS): $(OUT)/%.m.o: %.m
	@$(MKDIR_P) $(dir $@)
	$(CC) $(CPPFLAGS) $(CFLAGS) $(LIBGLFW3_PRIVATE_CPPFLAGS) -c $< -o $@

-include $(LIBGLFW3_OBJS:.o=.d)

endif
