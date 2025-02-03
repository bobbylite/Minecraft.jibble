use tray_icon::{
    menu::{Menu, MenuItem},
    Icon, TrayIconBuilder,
};
use winit::{
    event::{Event, WindowEvent},
    event_loop::{ControlFlow, EventLoop},
};
use std::path::{PathBuf};
use std::env;
use std::sync::{Arc, Mutex};

fn main() {
    // Create an event loop
    let event_loop = EventLoop::new();

    // Get the AppData directory
    let appdata_dir = env::var("APPDATA").expect("Failed to get APPDATA path");

    // Construct the path to the icon in AppData/.minecraft/jibble/
    let icon_path = PathBuf::from(format!("{}/.minecraft/jibble/icon.ico", appdata_dir));

    // Ensure the icon file exists
    if !icon_path.exists() {
        eprintln!("Error: Icon file not found at {:?}", icon_path);
        return;
    }

    // Load the icon
    let icon = Icon::from_path(&icon_path, None).expect("Failed to load icon");

    // Create a tray menu
    let menu = Menu::new();
    let exit_item = MenuItem::new("Exit", true, None);
    menu.append(&exit_item).unwrap();

    // Store a shared state for exiting
    let exit_flag = Arc::new(Mutex::new(false));

    // Clone exit_flag so the event loop can access it
    let exit_flag_clone = Arc::clone(&exit_flag);

    // Create the tray icon
    let _tray_icon = TrayIconBuilder::new()
        .with_menu(Box::new(menu))
        .with_tooltip("Rust Tray App")
        .with_icon(icon)
        .build()
        .unwrap();

    // Run the event loop
    event_loop.run(move |event, _, control_flow| {
        *control_flow = ControlFlow::Wait;

        // Check if the exit button was clicked
        if exit_item.is_enabled() && *exit_flag_clone.lock().unwrap() {
            println!("Exiting...");
            *control_flow = ControlFlow::ExitWithCode(0);
        }

        // Handle Window Events
        if let Event::WindowEvent { event, .. } = event {
            if let WindowEvent::CloseRequested = event {
                println!("Window close event received. Exiting...");
                *control_flow = ControlFlow::ExitWithCode(0);
            }
        }
    });

    // Set exit flag when "Exit" menu item is clicked (workaround for missing set_on_click)
    *exit_flag.lock().unwrap() = true;
}
