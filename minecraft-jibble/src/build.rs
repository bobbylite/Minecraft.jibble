fn main() {
    let mut res = winres::WindowsResource::new();
    res.set_icon("favicon.ico"); // This must be in your project root
    res.compile().expect("Failed to set application icon");
}
