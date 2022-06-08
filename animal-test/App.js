import * as React from "react";
import { WebView } from "react-native-webview";
import { StyleSheet } from "react-native";

export default function App() {
  return (
    <WebView
      style={styles.container}
      source={{ uri: "https://animalai.netlify.app" }}
    />
  );
}

const styles = StyleSheet.create({
  container: {
    marginTop: 20,
  },
});
